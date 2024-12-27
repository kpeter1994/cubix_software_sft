import unittest
from unittest import mock

from flask import Flask
from routes.auth import auth


class TestAuthRoutes(unittest.TestCase):
    def setUp(self):
        """Tesztkörnyezet beállítása."""
        app = Flask(__name__)
        app.register_blueprint(auth, url_prefix="/auth")
        self.client = app.test_client()

    def test_register_missing_data(self):
        """Regisztráció tesztelése hiányos adatokkal."""
        response = self.client.post("/auth/register", json={"username": "testuser"})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Hiányzó felhasználónév vagy jelszó", response.json["error"])

    def test_register_successful(self):
        """Sikeres regisztráció (mockolt controller)."""
        with unittest.mock.patch("controller.auth_controller.AuthController.register", return_value={"id": 1, "username": "testuser"}):
            response = self.client.post("/auth/register", json={"username": "testuser", "password": "testpass", "name": "Test User"})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json["username"], "testuser")

    def test_login_missing_data(self):
        """Bejelentkezés tesztelése hiányos adatokkal."""
        response = self.client.post("/auth/login", json={"username": "testuser"})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Hiányzó felhasználónév vagy jelszó", response.json["error"])

    def test_login_successful(self):
        """Sikeres bejelentkezés (mockolt controller)."""
        with unittest.mock.patch("controller.auth_controller.AuthController.login", return_value={"id": 1, "username": "testuser", "token": "fake-token"}):
            response = self.client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["username"], "testuser")
            self.assertIn("token", response.json)

if __name__ == "__main__":
    unittest.main()
