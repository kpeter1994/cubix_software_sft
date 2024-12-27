from model.share import Share
from model.portfolio import Portfolio

class PortfolioController:
    @staticmethod
    def create_portfolio(user_id, name, description=None):
        try:
            # Portfólió létrehozása
            portfolio = Portfolio.create_portfolio(user_id=user_id, name=name, description=description)

            # Sikeres válasz visszaadása
            return {
                "portfolio_id": portfolio.id,
                "user_id": portfolio.user_id,
                "created_at": portfolio.created_at.isoformat(),
                "message": "Portfólió sikeresen létrehozva!"
            }
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_portfolio(portfolio_id):
        portfolio = Portfolio.get_by_id(portfolio_id)
        if portfolio:
            return portfolio.to_dict()
        return {"error": "A portfólió nem található"}

    @staticmethod
    def get_user_portfolios(user_id):
        portfolios = Portfolio.get_by_user_id(user_id)
        return [portfolio.to_dict() for portfolio in portfolios]

    @staticmethod
    def add_shares_to_portfolio(user_id, portfolio_id, share_data):
        try:
            # Ellenőrizzük, hogy létezik-e a portfólió
            portfolio = Portfolio.get_by_id(portfolio_id)
            if not portfolio:
                return {"error": "Portfólió nem található"}

            # Ellenőrizzük, hogy a portfólió a helyes felhasználóhoz tartozik
            if portfolio.user_id != user_id:
                return {"error": "Ez a portfólió nem a felhasználóhoz tartozik"}

            # Share adatok hozzáadása a portfólióhoz
            for share in share_data:
                Share.create_share(
                    portfolio_id=portfolio.id,
                    share_id=share["share_id"],
                    cost_value=share["cost_value"],
                    quantity=share["quantity"],
                    date=share["date"]
                )

            return {"message": "Részvények sikeresen hozzáadva a portfólióhoz"}
        except Exception as e:
            return {"error": str(e)}