import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from controller.portfolio_controller import PortfolioController

class TestPortfolioController(unittest.TestCase):

    @patch("model.portfolio.Portfolio.create_portfolio")
    @patch("model.share.Share.create_share")
    def test_create_portfolio(self, mock_create_share, mock_create_portfolio):
        # Mockoljuk a Portfolio.create_portfolio metódust
        mock_portfolio = MagicMock()
        mock_portfolio.id = 1
        mock_portfolio.user_id = 1
        mock_portfolio.created_at = datetime.now()
        mock_create_portfolio.return_value = mock_portfolio

        # Tesztadatok
        user_id = 1
        # A share_data nem szükséges itt, mert a create_portfolio nem használja
        result = PortfolioController.create_portfolio(user_id, "Test Portfolio", "Test description")

        # Teszteljük, hogy a válasz megfelelő-e
        self.assertEqual(result["portfolio_id"], 1)
        self.assertEqual(result["user_id"], 1)
        self.assertIn("message", result)
        self.assertEqual(result["message"], "Portfólió sikeresen létrehozva!")

        # Ellenőrizzük, hogy a részvények hozzáadása nem történt meg itt
        mock_create_share.assert_not_called()

    @patch("model.portfolio.Portfolio.get_by_user_id")
    def test_get_user_portfolios(self, mock_get_by_user_id):
        # Mockoljuk a Portfolio.get_by_user_id metódust
        mock_portfolio_1 = MagicMock()
        mock_portfolio_1.to_dict.return_value = {
            "id": 1,
            "user_id": 1,
            "name": "Portfolio 1",
            "description": "First portfolio",
            "created_at": "2024-12-27T10:00:00"
        }
        mock_portfolio_2 = MagicMock()
        mock_portfolio_2.to_dict.return_value = {
            "id": 2,
            "user_id": 1,
            "name": "Portfolio 2",
            "description": "Second portfolio",
            "created_at": "2024-12-26T15:00:00"
        }

        mock_get_by_user_id.return_value = [mock_portfolio_1, mock_portfolio_2]

        # Tesztadatok
        user_id = 1

        # A controller metódus hívása
        portfolios = PortfolioController.get_user_portfolios(user_id)

        # Teszteljük, hogy a portfóliók helyesen vissza lettek adva
        self.assertEqual(len(portfolios), 2)
        self.assertEqual(portfolios[0]["name"], "Portfolio 1")
        self.assertEqual(portfolios[1]["name"], "Portfolio 2")

    @patch("model.portfolio.Portfolio.get_by_id")
    @patch("model.share.Share.create_share")
    def test_add_shares_to_portfolio(self, mock_create_share, mock_get_by_id):
        # Mockoljuk a Portfolio.get_by_id metódust
        mock_portfolio = MagicMock()
        mock_portfolio.id = 1
        mock_portfolio.user_id = 1
        mock_get_by_id.return_value = mock_portfolio

        # Mockoljuk a Share.create_share metódust
        mock_create_share.return_value = None  # Sikeres hozzáadás

        # Tesztadatok
        user_id = 1
        portfolio_id = 1
        share_data = [
            {"share_id": 101, "cost_value": 100.0, "quantity": 10, "date": "2024-12-27"},
            {"share_id": 102, "cost_value": 120.0, "quantity": 5, "date": "2024-12-27"}
        ]

        # A controller metódus hívása
        result = PortfolioController.add_shares_to_portfolio(user_id, portfolio_id, share_data)

        # Teszteljük, hogy a válasz megfelelő-e
        self.assertEqual(result["message"], "Részvények sikeresen hozzáadva a portfólióhoz")

        # Ellenőrizzük, hogy a részvények hozzáadása megtörtént
        mock_create_share.assert_any_call(
            portfolio_id=1,
            share_id=101,
            cost_value=100.0,
            quantity=10,
            date="2024-12-27"
        )
        mock_create_share.assert_any_call(
            portfolio_id=1,
            share_id=102,
            cost_value=120.0,
            quantity=5,
            date="2024-12-27"
        )

if __name__ == "__main__":
    unittest.main()
