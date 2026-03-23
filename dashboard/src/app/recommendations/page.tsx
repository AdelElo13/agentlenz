"use client";

import { useEffect, useState } from "react";
import { api, RecommendationsResponse } from "@/lib/api";

export default function RecommendationsPage() {
  const [recs, setRecs] = useState<RecommendationsResponse | null>(null);

  useEffect(() => { api.getRecommendations().then(setRecs).catch(console.error); }, []);

  if (!recs) return <p className="text-zinc-500">Loading...</p>;

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Model Routing Recommendations</h2>
      <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-6 mb-6">
        <p className="text-sm text-zinc-500">Total Potential Savings</p>
        <p className="text-4xl font-bold text-green-400">
          ${recs.total_potential_savings_usd.toFixed(2)}
        </p>
      </div>
      <div className="space-y-4">
        {recs.recommendations.map((rec, i) => (
          <div key={i} className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
            <div className="flex items-center gap-3 mb-3">
              <span className="font-mono text-sm text-red-400">{rec.current_model}</span>
              <span className="text-zinc-600">&rarr;</span>
              <span className="font-mono text-sm text-green-400">{rec.recommended_model}</span>
            </div>
            <p className="text-sm mb-2">{rec.reason}</p>
            <div className="flex gap-6 text-xs text-zinc-500">
              <span>Affected calls: {rec.affected_calls.toLocaleString()}</span>
              <span>Savings: {rec.estimated_savings_pct}%</span>
              <span className="text-green-400">
                ${rec.estimated_savings_usd.toFixed(2)}
              </span>
            </div>
          </div>
        ))}
        {recs.recommendations.length === 0 && (
          <p className="text-zinc-500">No recommendations yet. Send some agent data first.</p>
        )}
      </div>
    </div>
  );
}
