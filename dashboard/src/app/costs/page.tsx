"use client";

import { useEffect, useState } from "react";
import { api, CostResponse } from "@/lib/api";

export default function CostsPage() {
  const [costs, setCosts] = useState<CostResponse | null>(null);
  const [days, setDays] = useState(30);

  useEffect(() => { api.getCosts(days).then(setCosts).catch(console.error); }, [days]);

  if (!costs) return <p className="text-zinc-500">Loading...</p>;

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold">Cost Explorer</h2>
        <select
          value={days}
          onChange={(e) => setDays(Number(e.target.value))}
          className="bg-zinc-900 border border-zinc-700 rounded px-3 py-1 text-sm"
        >
          <option value={7}>Last 7 days</option>
          <option value={30}>Last 30 days</option>
          <option value={90}>Last 90 days</option>
        </select>
      </div>
      <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-6 mb-6">
        <p className="text-sm text-zinc-500">Total Spend</p>
        <p className="text-4xl font-bold">${costs.total_cost_usd.toFixed(2)}</p>
      </div>
      <table className="w-full text-sm">
        <thead>
          <tr className="text-zinc-500 border-b border-zinc-800">
            <th className="text-left py-2">Provider</th>
            <th className="text-left py-2">Model</th>
            <th className="text-right py-2">Input Tokens</th>
            <th className="text-right py-2">Output Tokens</th>
            <th className="text-right py-2">Calls</th>
            <th className="text-right py-2">Cost</th>
          </tr>
        </thead>
        <tbody>
          {costs.breakdown.map((row, i) => (
            <tr key={i} className="border-b border-zinc-800/50">
              <td className="py-2">{row.provider}</td>
              <td className="py-2 font-mono text-xs">{row.model}</td>
              <td className="text-right py-2">{row.total_input_tokens.toLocaleString()}</td>
              <td className="text-right py-2">{row.total_output_tokens.toLocaleString()}</td>
              <td className="text-right py-2">{row.call_count.toLocaleString()}</td>
              <td className="text-right py-2 font-medium">${row.total_cost_usd.toFixed(4)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
