"use client";

import { useEffect, useState } from "react";
import { api, WasteResponse } from "@/lib/api";

export default function WastePage() {
  const [waste, setWaste] = useState<WasteResponse | null>(null);

  useEffect(() => { api.getWaste().then(setWaste).catch(console.error); }, []);

  if (!waste) return <p className="text-zinc-500">Loading...</p>;

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Waste Report</h2>
      <div className="bg-green-900/20 border border-green-800 rounded-lg p-6 mb-6">
        <p className="text-sm text-green-400">Potential Savings</p>
        <p className="text-4xl font-bold text-green-400">
          ${waste.total_potential_savings_usd.toFixed(2)}
        </p>
      </div>
      <div className="space-y-4">
        {waste.items.map((item, i) => (
          <div key={i} className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
            <div className="flex justify-between items-start mb-2">
              <span className="text-xs font-mono bg-zinc-800 px-2 py-1 rounded">{item.type}</span>
              <span className="text-green-400 font-medium">
                Save ${item.potential_savings_usd.toFixed(2)}
              </span>
            </div>
            <p className="text-sm mb-2">{item.description}</p>
            <p className="text-xs text-zinc-500">
              Recommendation: {item.recommendation}
            </p>
          </div>
        ))}
        {waste.items.length === 0 && (
          <p className="text-zinc-500">No waste patterns detected. Nice work!</p>
        )}
      </div>
    </div>
  );
}
