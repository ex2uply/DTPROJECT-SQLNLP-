import { useState } from 'react';
import axios from 'axios';
import ChatInterface from './components/ChatInterface';
import ResultsDisplay from './components/ResultsDisplay';
import AnimatedBackground from './components/ui/AnimatedBackground';
import TypewriterTitle from './components/ui/TypewriterTitle';
import { motion } from 'framer-motion';

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
    <div className="min-h-screen text-white relative">
      <AnimatedBackground />
      
      <div className="container mx-auto px-4 py-16 relative z-10">
        {/* Header */}
        <div className="text-center mb-16">
          <motion.div 
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="inline-block mb-4 px-4 py-1.5 rounded-full bg-white text-black text-sm font-medium"
          >
            ✨ AI-Powered Database Assistant
          </motion.div>
          
          <TypewriterTitle 
            text="Ask Your Data Anything" 
            className="text-6xl md:text-7xl font-bold text-white mb-6 tracking-tight"
          />
          
          <motion.p 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1, duration: 1 }}
            className="text-gray-400 text-xl max-w-2xl mx-auto leading-relaxed"
          >
            Transform natural language into powerful insights. Just type your question and let our AI handle the complex SQL generation.
          </motion.p>
        </div>

        {/* Chat Interface */}
        <ChatInterface onSendQuery={handleQuery} isLoading={isLoading} />

        {/* Error Display */}
        {error && (
          <motion.div 
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="w-full max-w-3xl mx-auto mt-8"
          >
            <div className="bg-black border-2 border-white rounded-lg p-4 text-center">
              <p className="text-white font-medium">{error}</p>
            </div>
          </motion.div>
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
    </div>
  );
}

export default App;
