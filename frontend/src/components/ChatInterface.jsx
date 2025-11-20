import { useState } from 'react';
import { Send, Loader2, Sparkles } from 'lucide-react';
import { motion } from 'framer-motion';
import GlassCard from './ui/GlassCard';

export default function ChatInterface({ onSendQuery, isLoading }) {
  const [query, setQuery] = useState('');
  const [isFocused, setIsFocused] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim() && !isLoading) {
      onSendQuery(query);
      setQuery('');
    }
  };

  return (
    <div className="w-full max-w-3xl mx-auto relative z-10">
      <GlassCard className="p-2">
        <form onSubmit={handleSubmit} className="relative flex items-center">
          <div className="absolute left-4 text-white">
            <Sparkles className={`w-5 h-5 transition-all duration-300 ${isFocused ? 'opacity-100 scale-110' : 'opacity-50 scale-100'}`} />
          </div>
          
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onFocus={() => setIsFocused(true)}
            onBlur={() => setIsFocused(false)}
            placeholder="Ask anything about your data..."
            className="w-full bg-transparent text-white placeholder-gray-500 focus:outline-none text-lg py-4 pl-12 pr-16"
            disabled={isLoading}
          />
          
          <motion.button
            type="submit"
            disabled={isLoading || !query.trim()}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="absolute right-2 p-3 rounded-lg bg-white text-black hover:bg-gray-200 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isLoading ? (
              <Loader2 className="w-5 h-5 animate-spin" />
            ) : (
              <Send className="w-5 h-5" />
            )}
          </motion.button>
        </form>
      </GlassCard>
      
      {/* Helper chips */}
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="flex flex-wrap gap-2 justify-center mt-4"
      >
        {[
          "Total revenue by city in 2019",
          "Top 5 most expensive products sold",
          "Sales count for 'MacBook Pro Laptop'",
          "Monthly sales trend for San Francisco",
          "Average order value by product",
          "Orders with quantity greater than 2"
        ].map((suggestion, idx) => (
          <button
            key={idx}
            onClick={() => setQuery(suggestion)}
            className="px-3 py-1.5 text-xs rounded-full bg-black border border-white/20 text-gray-400 hover:bg-white hover:text-black transition-colors cursor-pointer"
          >
            {suggestion}
          </button>
        ))}
      </motion.div>
    </div>
  );
}
