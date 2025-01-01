from model.share import Share
from model.portfolio import Portfolio
from model.company import Company

from yfinance import Ticker
from peewee import DoesNotExist

class PortfolioController:
    @staticmethod
    def create_portfolio(user_id, name, description=None):
        try:
            portfolio = Portfolio.create_portfolio(user_id=user_id, name=name, description=description)

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
            portfolio = Portfolio.get_by_id(portfolio_id)
            if not portfolio:
                return {"error": "Portfólió nem található"}

            # Ellenőrizzük, hogy a portfólió a helyes felhasználóhoz tartozik
            if portfolio.user_id != user_id:
                return {"error": "Ez a portfólió nem a felhasználóhoz tartozik"}

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

    @staticmethod
    def delete_portfolio(user_id, portfolio_id):
        try:
            portfolio = Portfolio.get_by_id(portfolio_id)

            if portfolio.user_id != user_id:
                return {"error": "Ez a portfólió nem a felhasználóhoz tartozik"}

            portfolio.delete_instance()

            return {"message": "Portfólió sikeresen törölve"}

        except Portfolio.DoesNotExist:
            return {"error": "Portfólió nem található"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete_share_from_portfolio(user_id, portfolio_id, share_id):
        try:
            portfolio = Portfolio.get_by_id(portfolio_id)
            if not portfolio:
                return {"error": "Portfólió nem található"}

            if portfolio.user_id != user_id:
                return {"error": "Ez a portfólió nem a felhasználóhoz tartozik"}

            share = Share.get((Share.portfolio_id == portfolio_id) & (Share.id == share_id))
            if not share:
                return {"error": "Részvény nem található a portfólióban"}

            share.delete_instance()

            return {"message": "Részvény sikeresen törölve a portfólióból"}
        except Share.DoesNotExist:
            return {"error": "Részvény nem található a portfólióban"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_portfolio_details(portfolio_id):
        try:
            # Portfólió lekérdezése
            portfolio = Portfolio.get_or_none(Portfolio.id == portfolio_id)
            if not portfolio:
                return {"error": "A portfólió nem található"}

            # Részvények lekérdezése a portfólióhoz
            shares = Share.select().where(Share.portfolio_id == portfolio_id)
            if shares.count() == 0:
                return {"error": "Nincsenek részvények ebben a portfólióban"}

            portfolio_details = []
            for share in shares:
                try:
                    stock = Ticker(share.share_id)
                    current_price = stock.history(period="1d")["Close"].iloc[-1]
                    cost_value = share.cost_value
                    quantity = share.quantity

                    change = ((float(current_price) - float(cost_value)) / float(cost_value)) * 100

                    portfolio_details.append({
                        "id": share.id,
                        "share_id": share.share_id,
                        "cost_value": cost_value,
                        "current_price": float(current_price),
                        "change_percentage": round(change, 2),
                        "quantity": quantity
                    })
                except Exception as e:
                    # Hibakezelés adott részvényre
                    portfolio_details.append({
                        "share_id": share.share_id,
                        "error": f"Hiba a részvény adatainak lekérésekor: {str(e)}"
                    })

            return {
                "portfolio_name": portfolio.name,
                "portfolio_id": portfolio.id,
                "details": portfolio_details
            }

        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_current_stock_price(stock_symbol):
        try:
            stock = Ticker(stock_symbol)
            current_price = stock.history(period="1d")["Close"].iloc[-1]  # Utolsó záró ár
            return {"stock_symbol": stock_symbol, "current_price": float(current_price)}
        except Exception as e:
            return {"error": f"Nem sikerült lekérni az aktuális árfolyamot: {str(e)}"}

    @staticmethod
    def search_stock(query):
        """
        Keresés cégnév vagy szimbólum alapján a peewee ORM segítségével.
        """
        try:
            company = Company.select().where(
                (Company.name.contains(query)) | (Company.symbol == query.upper())
            ).first()

            if company:
                symbol = company.symbol
                stock = Ticker(symbol)
                info = stock.info
                market_price = info.get("regularMarketPrice") or info.get("previousClose") or "N/A"

                return {
                    "symbol": info.get("symbol", symbol),
                    "name": info.get("longName", company.name),
                    "sector": info.get("sector", "N/A"),
                    "currency": info.get("currency", "N/A"),
                    "market_price": market_price
                }

            return {"error": "Nincs találat a keresési kifejezésre."}

        except DoesNotExist:
            return {"error": "Nincs találat a keresési kifejezésre."}
