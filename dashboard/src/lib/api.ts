const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

async function fetchApi<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${process.env.NEXT_PUBLIC_API_KEY || ""}`,
      ...options?.headers,
    },
  });
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return res.json();
}

export interface CostBreakdown {
  provider: string;
  model: string;
  total_cost_usd: number;
  total_input_tokens: number;
  total_output_tokens: number;
  call_count: number;
}

export interface CostResponse {
  total_cost_usd: number;
  breakdown: CostBreakdown[];
  period_start: string;
  period_end: string;
}

export interface WasteItem {
  type: string;
  description: string;
  potential_savings_usd: number;
  affected_traces: number;
  recommendation: string;
}

export interface WasteResponse {
  total_potential_savings_usd: number;
  items: WasteItem[];
}

export interface Recommendation {
  current_model: string;
  recommended_model: string;
  estimated_savings_pct: number;
  estimated_savings_usd: number;
  affected_calls: number;
  reason: string;
}

export interface RecommendationsResponse {
  recommendations: Recommendation[];
  total_potential_savings_usd: number;
}

export interface Budget {
  id: string;
  name: string;
  max_cost_usd: number;
  period: string;
  is_active: boolean;
  current_spend_usd: number;
  created_at: string;
}

export const api = {
  getCosts: (days = 30) => fetchApi<CostResponse>(`/v1/costs?days=${days}`),
  getWaste: (days = 30) => fetchApi<WasteResponse>(`/v1/waste?days=${days}`),
  getRecommendations: (days = 30) =>
    fetchApi<RecommendationsResponse>(`/v1/recommendations?days=${days}`),
  getBudgets: () => fetchApi<Budget[]>("/v1/budgets"),
  createBudget: (data: { name: string; max_cost_usd: number; period?: string }) =>
    fetchApi<Budget>("/v1/budgets", { method: "POST", body: JSON.stringify(data) }),
  deleteBudget: (id: string) =>
    fetchApi<void>(`/v1/budgets/${id}`, { method: "DELETE" }),
};
