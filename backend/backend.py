from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from database import initialize_database  # Import az adatbázis inicializációhoz

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['JWT_SECRET_KEY'] = '5f2c0833b5f4d09e2e6c13c9897ff9d88a30c4550e39c3e1124d49db56b8f1d2'
    jwt = JWTManager(app)

    # Az alkalmazás útvonalai (pl. auth, portfolio) importálhatók itt:
    from auth_controller import auth_bp
    from portfolio_controller import portfolio_bp

    # Regisztráld a Blueprint-eket
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(portfolio_bp, url_prefix='/portfolio')
    return app

if __name__ == "__main__":
    # Adatbázis inicializálása indulás előtt
    initialize_database()

    # Flask alkalmazás létrehozása és futtatása
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
