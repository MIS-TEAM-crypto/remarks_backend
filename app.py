from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

GAS_URL = "https://script.google.com/macros/s/AKfycbyBg-cWHerhIDEhcSIyVQarMgb7Qhjim3dvaw90zdqHbQbFokrEeflKbOV8NUoPoz1ZSw/exec"

@app.route("/api", methods=["GET"])
def api():
    response = requests.get(GAS_URL, params=request.args)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(port=5000, debug=True)
