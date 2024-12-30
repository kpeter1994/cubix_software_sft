export interface Portfolio {
  created_at: string;
  id: string;
  user_id: string;
  name: string;
  description: string;
}

export interface PortfolioResponse {
  portfolios: Portfolio[];
}