# 🚀 Leak Sniffer

A fast and efficient Streamlit-based web application for searching domain-related data breaches and leaked credentials from MongoDB collections. This tool helps security professionals and researchers quickly identify potential security exposures for specific domains.

## ✨ Features

- **Fast Multi-threaded Search**: Utilizes concurrent processing to search across multiple MongoDB collections simultaneously
- **Interactive Web Interface**: Clean and intuitive Streamlit-based UI
- **Bulk Data Export**: Download search results as CSV files
- **Real-time Results**: Live display of search progress and results
- **Domain-based Filtering**: Search for specific domains across all available leak databases
- **Optimized Queries**: Efficient MongoDB queries with field projection for better performance

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Database**: MongoDB
- **Backend**: Python 3.x
- **Data Processing**: Pandas
- **Concurrency**: ThreadPoolExecutor

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher
- MongoDB server running (local or remote)
- MongoDB collections containing leak data with the following schema:
  ```json
  {
    "Domain": "example.com",
    "URL": "https://example.com/login",
    "Username": "user@example.com", 
    "Password": "password123"
  }
  ```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/LkSniffer.git
   cd LkSniffer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB connection**
   
   You can configure the MongoDB connection in several ways:
   
   **Option 1: Environment Variables**
   ```bash
   export MONGO_URI="mongodb://localhost:27017/"
   export DATABASE_NAME="Test"
   export MAX_WORKERS="16"
   ```
   
   **Option 2: Edit config.py**
   Modify the values in `config.py` according to your setup.

## 🎯 Usage

1. **Start the application**
   ```bash
   streamlit run Leaksniffer.py
   ```

2. **Access the web interface**
   Open your browser and navigate to `http://localhost:8501`

3. **Search for domain leaks**
   - Enter a domain name (e.g., `example.com`)
   - Click the "Search" button
   - View results in the interactive table
   - Download results as CSV if needed

## ⚙️ Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `MONGO_URI` | `mongodb://localhost:27017/` | MongoDB connection string |
| `DATABASE_NAME` | `Test` | Name of the MongoDB database |
| `MAX_WORKERS` | `16` | Number of concurrent threads for searching |

### MongoDB Setup

Ensure your MongoDB instance contains collections with leak data. The application will automatically discover and search all collections in the specified database.

**Expected document structure:**
```json
{
  "Domain": "target-domain.com",
  "URL": "https://target-domain.com/path",
  "Username": "user@target-domain.com",
  "Password": "leaked-password"
}
```

## 🔧 Project Structure

```
LkSniffer/
├── Leaksniffer.py      # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
├── README.md          # Project documentation
└── LICENSE            # License file
```

## 🚨 Security Considerations

⚠️ **Important Security Notes:**

- This tool is intended for **authorized security research and testing only**
- Ensure you have proper authorization before searching any domain
- Keep your MongoDB instance secure and properly configured
- Consider implementing authentication and access controls
- Do not expose this tool to public networks without proper security measures
- Be aware of data privacy laws and regulations in your jurisdiction

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is provided for educational and authorized security testing purposes only. Users are responsible for ensuring they have proper authorization before using this tool to search for any domain-related data. The developers are not responsible for any misuse of this tool.

## 🐛 Known Issues

- Large result sets may cause memory issues - consider implementing pagination for production use
- No built-in authentication - implement proper access controls for production deployment

## 🔮 Future Enhancements

- [ ] User authentication and authorization
- [ ] Result pagination for large datasets
- [ ] Advanced search filters (date ranges, data types)
- [ ] Data visualization and analytics
- [ ] API endpoints for programmatic access
- [ ] Scheduled scanning capabilities
- [ ] Integration with threat intelligence feeds

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact the maintainers.

---

**Made with ❤️ for the cybersecurity community** 