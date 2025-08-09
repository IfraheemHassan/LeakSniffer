import streamlit as st
from pymongo import MongoClient
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import (
    MONGO_URI, DATABASE_NAME, MAX_WORKERS, 
    PAGE_TITLE, APP_TITLE, DEFAULT_PROJECTION, COLUMN_ORDER
)

# ------------------ Database Functions ------------------ #
@st.cache_resource
def get_db():
    """Get MongoDB database connection with caching."""
    client = MongoClient(MONGO_URI)
    return client[DATABASE_NAME]

def search_in_collection(collection, domain):
    """Search for domain matches in a specific collection."""
    try:
        query = {"Domain": domain}
        return list(collection.find(query, DEFAULT_PROJECTION))
    except Exception as e:
        st.error(f"Error searching collection: {str(e)}")
        return []

def fast_search(db, domain):
    """Perform concurrent search across all collections."""
    collections = db.list_collection_names()
    all_results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [
            executor.submit(search_in_collection, db[collection_name], domain) 
            for collection_name in collections
        ]
        for future in as_completed(futures):
            all_results.extend(future.result())

    return all_results

# ------------------ UI Components ------------------ #
def setup_page():
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title=PAGE_TITLE, 
        layout="wide",
        page_icon="🔍"
    )
    st.title(APP_TITLE)
    st.markdown("*Search for domain-related leaked credentials across multiple databases*")

def display_results(results, domain):
    """Display search results in a formatted table with download option."""
    df = pd.DataFrame(results)
    
    # Ensure consistent column order
    for col in COLUMN_ORDER:
        if col not in df.columns:
            df[col] = ""
    
    # Reorder columns
    df = df[COLUMN_ORDER + [c for c in df.columns if c not in COLUMN_ORDER]]
    
    st.success(f"✅ Found {len(df)} matching records for domain: **{domain}**")
    st.dataframe(df, use_container_width=True)
    
    # Download functionality
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Results as CSV",
        data=csv,
        file_name=f"{domain.strip()}_leaks.csv",
        mime="text/csv",
        help="Download search results in CSV format"
    )

# ------------------ Main Application ------------------ #
def main():
    """Main application function."""
    setup_page()
    
    # Input section
    st.subheader("🔍 Domain Search")
    domain = st.text_input(
        "Enter domain to search for leaked credentials:",
        placeholder="example.com",
        help="Enter the domain name without protocol (e.g., google.com, not https://google.com)"
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        search_button = st.button("🚀 Search", type="primary")
    
    # Search functionality
    if search_button:
        if not domain.strip():
            st.warning("⚠️ Please enter a domain name to search.")
        else:
            with st.spinner(f"🔍 Searching for '{domain.strip()}' across all databases..."):
                try:
                    db = get_db()
                    results = fast_search(db, domain.strip())
                    
                    if results:
                        display_results(results, domain.strip())
                    else:
                        st.info("🧼 No leaked records found for this domain.")
                        st.markdown("*This could mean:*")
                        st.markdown("- The domain has no known data breaches")
                        st.markdown("- The domain is not in our current database")
                        st.markdown("- Try variations of the domain name")
                        
                except Exception as e:
                    st.error(f"❌ An error occurred during search: {str(e)}")
                    st.markdown("*Please check your MongoDB connection and try again.*")

    # Information section
    with st.expander("ℹ️ About this tool"):
        st.markdown("""
        **Leak Sniffer** helps security professionals identify potential data exposures for specific domains.
        
        **Features:**
        - Fast multi-threaded search across MongoDB collections
        - Export results to CSV format
        - Clean and intuitive interface
        
        **Security Note:** This tool is intended for authorized security research only. 
        Ensure you have proper authorization before searching any domain.
        """)

if __name__ == "__main__":
    main()