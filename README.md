# AI/ML Database Query System

Transform natural language into powerful SQL queries with this full-stack application featuring AI-powered query generation, automatic execution, and interactive data visualizations.

![Application Demo](https://img.shields.io/badge/Status-Production%20Ready-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![React](https://img.shields.io/badge/React-19.2.0-61dafb)

## 🌟 Features

- **Natural Language Processing**: Ask questions in plain English
- **Automatic SQL Generation**: AI-powered query translation
- **Interactive Visualizations**: Beautiful charts with Recharts
- **Real-time Results**: Instant query execution and display
- **Modern UI**: Glassmorphic design with Tailwind CSS v4
- **Sample Database**: Pre-loaded SQLite database with sales data

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/ex2uply/DTPROJECT-SQLNLP-.git
cd DTPROJECT-SQLNLP-
```

2. **Set up Backend**
```bash
cd backend
pip install -r requirements.txt
```

3. **Set up Frontend**
```bash
cd frontend
npm install
```

### Running the Application

1. **Start the Backend Server**
```bash
cd backend
python main.py
```
Backend runs on `http://localhost:8000`

2. **Start the Frontend (in a new terminal)**
```bash
cd frontend
npm run dev
```
Frontend runs on `http://localhost:5173`

3. **Open your browser** to `http://localhost:5173`

## 💡 Usage Examples

Try these natural language queries:
- "Show me all sales"
- "Count sales by product"
- "Sales data for laptops"
- "Total revenue by date"

## 🏗️ Architecture

### Backend Stack
- **FastAPI**: High-performance web framework
- **SQLite**: Lightweight database
- **Pandas**: Data manipulation and analysis
- **Python Modules**:
  - `nlp_engine.py`: Natural language processing
  - `db_manager.py`: Database operations
  - `reporting.py`: Chart configuration and data analysis

### Frontend Stack
- **React 19**: Modern UI framework
- **Vite**: Fast build tool
- **Tailwind CSS v4**: Utility-first styling
- **Recharts**: Data visualization
- **Axios**: HTTP client
- **Lucide React**: Icon library

## 📁 Project Structure

```
DTPROJECT-SQLNLP-/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── db_manager.py        # Database operations
│   ├── nlp_engine.py        # NLP & SQL generation
│   ├── reporting.py         # Chart configuration
│   ├── requirements.txt     # Python dependencies
│   └── example.db          # SQLite database (auto-created)
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatInterface.jsx
│   │   │   └── ResultsDisplay.jsx
│   │   ├── App.jsx
│   │   └── index.css
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md
```

## 🔧 Configuration

### Backend API Endpoints
- `GET /`: Welcome message
- `GET /health`: Health check
- `POST /query`: Process natural language query

### Frontend Environment
Update the API URL in `frontend/src/App.jsx` if deploying to production:
```javascript
const response = await axios.post('http://localhost:8000/query', {
  query: query
});
```

## 🎨 Screenshots

The application features a modern, dark-themed interface with:
- Gradient backgrounds
- Glassmorphic input fields
- Interactive data tables
- Dynamic chart visualizations
- Real-time SQL query display

## 🔮 Future Enhancements

- [ ] OpenAI/Gemini integration for advanced NLP
- [ ] Support for PostgreSQL, MySQL databases
- [ ] User authentication and query history
- [ ] Export reports (PDF, Excel)
- [ ] Multiple chart types (pie, scatter, area)
- [ ] Natural language report generation

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👨‍💻 Developer

Built with ❤️ using FastAPI, React, and Tailwind CSS

---

**Note**: This is a demonstration project. For production use, implement proper authentication, input validation, and SQL injection prevention.
