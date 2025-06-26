from flask import Flask, request, jsonify
import requests, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

API_URL = "https://stablediffusionapi.com/api/v4/dreambooth"
API_KEY = os.getenv("API_KEY")
STYLE = os.getenv("AGENT_STYLE", "dreamlike chaos")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    styled = f"{prompt}, style of {STYLE}"

    payload = {"prompt": styled, "api_key": API_KEY}
    resp = requests.post(API_URL, json=payload)
    if resp.ok:
        return jsonify(resp.json())
    return jsonify({"error": "Failed", "details": resp.text}), 400

if __name__ == "__main__":
    app.run(debug=True)
add backend app.py
