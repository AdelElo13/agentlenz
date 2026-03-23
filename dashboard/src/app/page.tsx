"use client";

import { useEffect, useState } from "react";
import { api, CostResponse, WasteResponse, RecommendationsResponse } from "@/lib/api";

export default function OverviewPage() {
  const [costs, setCosts] = useState<CostResponse | null>(null);
  const [waste, setWaste] = useState<WasteResponse | null>(null);
  const [recs, setRecs] = useState<RecommendationsResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([api.getCosts(), api.getWaste(), api.getRecommendations()])
      .then(([c, w, r]) => { setCosts(c); setWaste(w); setRecs(r); })
      .catch((e) => setError(e.message));
  }, []);

  if (error) return <p className="text-red-400">Error: {error}</p>;
  if (!costs) return <p className="text-zinc-500">Loading...</p>;

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Overview</h2>
      <div className="grid grid-cols-3 gap-4 mb-8">
        <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-6">
          <p className="text-sm text-zinc-500">Total Spend (30d)</p>
          <p className="text-3xl font-bold">${costs.total_cost_usd.toFixed(2)}</p>
        </div>
        <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-6">
          <p className="text-sm text-zinc-500">Potential Savings</p>
          <p className="text-3xl font-bold text-green-400">
            ${(waste?.total_potential_savings_usd ?? 0).toFixed(2)}
          </p>
        </div>
        <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-6">
          <p className="text-sm text-zinc-500">Recommendations</p>
          <p className="text-3xl font-bold">{recs?.recommendations.length ?? 0}</p>
        </div>
      </div>
      <h3 className="text-lg font-semibold mb-3">Cost Breakdown by Model</h3>
      <table className="w-full text-sm">
        <thead>
          <tr className="text-zinc-500 border-b border-zinc-800">
            <th className="text-left py-2">Provider</th>
            <th className="text-left py-2">Model</th>
            <th className="text-right py-2">Calls</th>
            <th className="text-right py-2">Cost</th>
          </tr>
        </thead>
        <tbody>
          {costs.breakdown.map((row, i) => (
            <tr key={i} className="border-b border-zinc-800/50">
              <td className="py-2">{row.provider}</td>
              <td className="py-2">{row.model}</td>
              <td className="text-right py-2">{row.call_count.toLocaleString()}</td>
              <td className="text-right py-2">${row.total_cost_usd.toFixed(4)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
