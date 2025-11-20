import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Database, TrendingUp, Table as TableIcon } from 'lucide-react';
import GlassCard from './ui/GlassCard';

export default function ResultsDisplay({ data, sql, chartData }) {
  if (!data || data.length === 0) return null;

  return (
    <div className="w-full max-w-6xl mx-auto mt-12 space-y-8 pb-20">
      {/* SQL Display */}
      <GlassCard className="p-6 border-l-4 border-l-white">
        <h3 className="text-xs font-bold uppercase tracking-wider text-white mb-3 flex items-center gap-2">
          <Database className="w-4 h-4" />
          Generated SQL
        </h3>
        <div className="bg-white/5 rounded-lg p-4 font-mono text-sm text-white overflow-x-auto border border-white/10">
          {sql}
        </div>
      </GlassCard>

      {/* Chart Display - REMOVED per user request */}


      {/* Table Display */}
      <GlassCard className="overflow-hidden">
        <div className="p-6 border-b border-white/10 flex items-center gap-3">
          <div className="p-2 rounded-lg bg-white text-black">
            <TableIcon className="w-6 h-6" />
          </div>
          <h3 className="text-xl font-bold text-white">Data Results</h3>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-white/5">
              <tr>
                {Object.keys(data[0]).map((key) => (
                  <th key={key} className="px-6 py-4 text-left text-xs font-bold text-white uppercase tracking-wider">
                    {key}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className="divide-y divide-white/10">
              {data.map((row, idx) => (
                <tr key={idx} className="hover:bg-white/5 transition-colors">
                  {Object.values(row).map((value, vidx) => (
                    <td key={vidx} className="px-6 py-4 text-sm text-white whitespace-nowrap">
                      {typeof value === 'object' ? JSON.stringify(value) : String(value)}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </GlassCard>
    </div>
  );
}
