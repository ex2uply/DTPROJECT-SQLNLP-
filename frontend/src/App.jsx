import { useState } from 'react';
import axios from 'axios';
import ChatInterface from './components/ChatInterface';
import ResultsDisplay from './components/ResultsDisplay';
import { Sparkles } from 'lucide-react';

function App() {
  const [results, setResults] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleQuery = async (query) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await axios.post('http://localhost:8000/query', {
        query: query
      });
      
      setResults({
        data: response.data.results,
        sql: response.data.sql,
        chartData: response.data.chart_data
      });
    } catch (err) {
      setError(err.response?.data?.error || err.message || 'Failed to process query');
      console.error('Query error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen p-8">
      {/* Header */}
      <div className="text-center mb-12">
        <div className="flex items-center justify-center gap-3 mb-4">
          <Sparkles className="w-10 h-10 text-blue-400" />
          <h1 className="text-5xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
            AI/ML Database Query System
          </h1>
        </div>
        <p className="text-gray-400 text-lg max-w-2xl mx-auto">
          Transform natural language into powerful SQL queries. Get instant insights with interactive visualizations.
        </p>
      </div>

      {/* Chat Interface */}
      <ChatInterface onSendQuery={handleQuery} isLoading={isLoading} />

      {/* Error Display */}
      {error && (
        <div className="w-full max-w-4xl mx-auto mt-6">
          <div className="backdrop-blur-xl bg-red-500/10 border border-red-500/30 rounded-2xl p-4">
            <p className="text-red-400 text-center">{error}</p>
          </div>
        </div>
      )}

      {/* Results Display */}
      {results && (
        <ResultsDisplay 
          data={results.data} 
          sql={results.sql} 
          chartData={results.chartData}
        />
      )}
    </div>
  );
}

export default App;
