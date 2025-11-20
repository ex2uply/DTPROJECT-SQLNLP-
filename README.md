# AI-Powered Database Query System

A full-stack application that allows users to query a sales database using natural language. The system uses Google's Gemini 2.0 Flash LLM to convert English questions into SQL queries, executes them against a local SQLite database, and displays the results in a clean, minimal interface.

## Features

- **Natural Language Processing**: Converts questions like "Show me sales in San Francisco" into valid SQL.
- **Context-Aware**: The AI understands the specific data in your database (e.g., city names, product types).
- **Local Data Processing**: Loads data from `Sales Data.csv` (185,000+ records) into a local SQLite database.
- **Minimal UI**: A clean, black-and-white dark mode interface built with React and Tailwind CSS.
- **Secure Configuration**: Uses `.env` files for API key management.

## Tech Stack

- **Frontend**: React, Tailwind CSS, Framer Motion, Lucide Icons
- **Backend**: Python, FastAPI, SQLite, Pandas
- **AI/LLM**: Google Gemini 2.0 Flash (via `google-generativeai`)

## Prerequisites

- Node.js (v16+)
- Python (v3.8+)
- Google Gemini API Key

## Setup Instructions

### Quick Start (Recommended)

1. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

2. Create a `.env` file in the `backend` directory:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

3. Install frontend dependencies:
```bash
cd frontend
npm install
```

4. Install root dependencies and start both servers:
```bash
cd ..
npm install
npm run dev
```

This will start both the backend (port 8000) and frontend (port 5173) simultaneously. Open your browser to `http://localhost:5173`.

### Manual Setup (Alternative)

If you prefer to run the servers separately:

**Backend:**
```bash
cd backend
pip install -r requirements.txt
# Create .env file with GEMINI_API_KEY
python main.py
```

**Frontend (in a new terminal):**
```bash
cd frontend
npm install
npm run dev
```

## Usage

1. Type a question in the search bar (e.g., "What is the total revenue by product?").
2. The system will generate the corresponding SQL query.
3. Results will be displayed in a table format.

## Project Structure

- `backend/`: Contains the FastAPI application, database logic, and NLP engine.
- `frontend/`: Contains the React application and UI components.
- `Sales Data.csv`: The source dataset used by the application.
