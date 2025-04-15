
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_BASE = "https://test-aoc.araymond.com.cn/seeyon/rest"

@app.route("/token", methods=["POST"])
def proxy_token():
    resp = requests.post(f"{API_BASE}/token", json=request.get_json())
    return (resp.text, resp.status_code, resp.headers.items())

@app.route("/start", methods=["POST"])
def proxy_start():
    token = request.headers.get("token")
    headers = {"Content-Type": "application/json", "token": token}
    resp = requests.post(f"{API_BASE}/bpm/process/start", json=request.get_json(), headers=headers)
    return (resp.text, resp.status_code, resp.headers.items())

@app.route("/")
def home():
    return "ESP32 API Proxy is running!"
