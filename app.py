from flask import Flask, request, make_response
from flask_cors import CORS
import requests

app = Flask(__name__)

# ✅ Explicit CORS config (important for Render)
CORS(
    app,
    resources={r"/api": {"origins": "*"}},
    supports_credentials=False
)

GAS_URL = "https://script.google.com/macros/s/AKfycbyBg-cWHerhIDEhcSIyVQarMgb7Qhjim3dvaw90zdqHbQbFokrEeflKbOV8NUoPoz1ZSw/exec"


@app.route("/api", methods=["GET", "OPTIONS"])
def api():

    # 🔹 Handle preflight request
    if request.method == "OPTIONS":
        response = make_response("", 204)
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    # 🔹 Forward request to Google Apps Script
    gas_response = requests.get(GAS_URL, params=request.args)

    # 🔹 Always return JSON + CORS headers
    response = make_response(
        gas_response.text,
        gas_response.status_code
    )
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"

    return response


# ⚠️ Not used on Render, but kept for local testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
