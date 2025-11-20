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

### 1. Backend Setup

Navigate to the backend directory and install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in the `backend` directory with your API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

Start the backend server:

```bash
python main.py
```

The server will start at `http://0.0.0.0:8000`. On the first run, it will automatically load the `Sales Data.csv` file into the database.

### 2. Frontend Setup

Navigate to the frontend directory and install dependencies:

```bash
cd frontend
npm install
```

Start the development server:

```bash
npm run dev
```

Open your browser to `http://localhost:5173`.

## Usage

1. Type a question in the search bar (e.g., "What is the total revenue by product?").
2. The system will generate the corresponding SQL query.
3. Results will be displayed in a table format.

## Project Structure

- `backend/`: Contains the FastAPI application, database logic, and NLP engine.
- `frontend/`: Contains the React application and UI components.
- `Sales Data.csv`: The source dataset used by the application.
