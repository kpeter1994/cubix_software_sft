from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.auth import auth
from routes.stock import stock


app = Flask(__name__)

CORS(app)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the API!"}), 200

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(stock, url_prefix="/stock")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")