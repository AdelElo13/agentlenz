"use client";

import { useEffect, useState } from "react";
import { api, Budget } from "@/lib/api";

export default function BudgetsPage() {
  const [budgets, setBudgets] = useState<Budget[]>([]);
  const [name, setName] = useState("");
  const [maxCost, setMaxCost] = useState("");
  const [period, setPeriod] = useState("monthly");

  const loadBudgets = () => api.getBudgets().then(setBudgets).catch(console.error);

  useEffect(() => { loadBudgets(); }, []);

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    await api.createBudget({ name, max_cost_usd: parseFloat(maxCost), period });
    setName("");
    setMaxCost("");
    loadBudgets();
  };

  const handleDelete = async (id: string) => {
    await api.deleteBudget(id);
    loadBudgets();
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Budgets</h2>
      <form onSubmit={handleCreate} className="bg-zinc-900 border border-zinc-800 rounded-lg p-5 mb-6">
        <h3 className="text-sm font-semibold mb-3">Create Budget</h3>
        <div className="flex gap-3">
          <input
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Budget name"
            className="bg-zinc-800 border border-zinc-700 rounded px-3 py-2 text-sm flex-1"
            required
          />
          <input
            value={maxCost}
            onChange={(e) => setMaxCost(e.target.value)}
            placeholder="Max cost (USD)"
            type="number"
            step="0.01"
            className="bg-zinc-800 border border-zinc-700 rounded px-3 py-2 text-sm w-40"
            required
          />
          <select
            value={period}
            onChange={(e) => setPeriod(e.target.value)}
            className="bg-zinc-800 border border-zinc-700 rounded px-3 py-2 text-sm"
          >
            <option value="daily">Daily</option>
            <option value="weekly">Weekly</option>
            <option value="monthly">Monthly</option>
          </select>
          <button
            type="submit"
            className="bg-white text-black px-4 py-2 rounded text-sm font-medium hover:bg-zinc-200"
          >
            Create
          </button>
        </div>
      </form>
      <div className="space-y-3">
        {budgets.map((budget) => (
          <div
            key={budget.id}
            className="bg-zinc-900 border border-zinc-800 rounded-lg p-4 flex justify-between items-center"
          >
            <div>
              <p className="font-medium">{budget.name}</p>
              <p className="text-sm text-zinc-500">
                ${budget.max_cost_usd.toFixed(2)} / {budget.period}
              </p>
            </div>
            <button
              onClick={() => handleDelete(budget.id)}
              className="text-red-400 text-sm hover:text-red-300"
            >
              Delete
            </button>
          </div>
        ))}
        {budgets.length === 0 && (
          <p className="text-zinc-500">No budgets configured yet.</p>
        )}
      </div>
    </div>
  );
}
