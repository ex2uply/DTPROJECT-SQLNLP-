import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Database, TrendingUp } from 'lucide-react';

export default function ResultsDisplay({ data, sql, chartData }) {
  if (!data || data.length === 0) {
    return (
      <div className="w-full max-w-4xl mx-auto mt-8">
        <div className="backdrop-blur-xl bg-white/5 rounded-2xl border border-white/20 p-12 text-center">
          <Database className="w-16 h-16 mx-auto mb-4 text-gray-400" />
          <p className="text-gray-400 text-lg">No results yet. Try asking a question!</p>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full max-w-6xl mx-auto mt-8 space-y-6">
      {/* SQL Display */}
      <div className="backdrop-blur-xl bg-white/5 rounded-2xl border border-white/20 p-6">
        <h3 className="text-sm font-semibold text-gray-400 mb-2 flex items-center gap-2">
          <Database className="w-4 h-4" />
          Generated SQL
        </h3>
        <pre className="bg-black/30 rounded-lg p-4 overflow-x-auto">
          <code className="text-green-400 text-sm font-mono">{sql}</code>
        </pre>
      </div>

      {/* Chart Display */}
      {chartData && chartData.type !== 'table' && chartData.x_axis && chartData.y_axis && (
        <div className="backdrop-blur-xl bg-white/5 rounded-2xl border border-white/20 p-8">
          <h3 className="text-lg font-semibold text-white mb-6 flex items-center gap-2">
            <TrendingUp className="w-5 h-5" />
            {chartData.title || 'Visualization'}
          </h3>
          <ResponsiveContainer width="100%" height={350}>
            {chartData.type === 'line' ? (
              <LineChart data={data}>
                <CartesianGrid strokeDasharray="3 3" stroke="#ffffff20" />
                <XAxis dataKey={chartData.x_axis} stroke="#9ca3af" />
                <YAxis stroke="#9ca3af" />
                <Tooltip 
                  contentStyle={{ 
                    backgroundColor: '#1e293b', 
                    border: '1px solid rgba(255,255,255,0.2)',
                    borderRadius: '8px'
                  }} 
                />
                <Legend />
                <Line 
                  type="monotone" 
                  dataKey={chartData.y_axis} 
                  stroke="#3b82f6" 
                  strokeWidth={3}
                  dot={{ fill: '#3b82f6', r: 4 }}
                />
              </LineChart>
            ) : (
              <BarChart data={data}>
                <CartesianGrid strokeDasharray="3 3" stroke="#ffffff20" />
                <XAxis dataKey={chartData.x_axis} stroke="#9ca3af" />
                <YAxis stroke="#9ca3af" />
                <Tooltip 
                  contentStyle={{ 
                    backgroundColor: '#1e293b', 
                    border: '1px solid rgba(255,255,255,0.2)',
                    borderRadius: '8px'
                  }} 
                />
                <Legend />
                <Bar dataKey={chartData.y_axis} fill="url(#colorGradient)" radius={[8, 8, 0, 0]} />
                <defs>
                  <linearGradient id="colorGradient" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#3b82f6" />
                    <stop offset="100%" stopColor="#8b5cf6" />
                  </linearGradient>
                </defs>
              </BarChart>
            )}
          </ResponsiveContainer>
        </div>
      )}

      {/* Table Display */}
      <div className="backdrop-blur-xl bg-white/5 rounded-2xl border border-white/20 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-white/5 border-b border-white/20">
              <tr>
                {Object.keys(data[0]).map((key) => (
                  <th key={key} className="px-6 py-4 text-left text-sm font-semibold text-gray-300">
                    {key}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((row, idx) => (
                <tr key={idx} className="border-b border-white/10 hover:bg-white/5 transition-colors">
                  {Object.values(row).map((value, vidx) => (
                    <td key={vidx} className="px-6 py-4 text-sm text-gray-200">
                      {typeof value === 'object' ? JSON.stringify(value) : String(value)}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
