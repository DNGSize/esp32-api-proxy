from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)

API_BASE = "https://test-aoc.araymond.com.cn/seeyon/rest"

@app.route("/token", methods=["POST"])
def proxy_token():
    resp = requests.post(f"{API_BASE}/token", json=request.get_json())
    return (resp.text, resp.status_code, resp.headers.items())

@app.route('/start-process', methods=['POST'])
def start_process():
    data = request.get_json()
    token = data.get('token')
    key = data.get('key')

    payload = {
        "appName": "collaboration",
        "data": {
            "data": {
                "formmain_1320": {
                    "Key1": key
                }
            },
            "templateCode": "Test_form",
            "draft": "0"
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'token': token
    }

    response = requests.post(
        'https://test-aoc.araymond.com.cn/seeyon/rest/bpm/process/start',
        headers=headers,
        data=json.dumps(payload)
    )

    return (response.text, response.status_code, response.headers.items())

@app.route("/")
def home():
    return "ESP32 API Proxy is running!"
    @app.route("/test", methods=["GET"])
def test_vpn():
    try:
        resp = requests.get("http://10.10.10.1:5000")  # or any port your server listens on
        return f"VPN connection OK: {resp.text}", 200
    except Exception as e:
        return f"VPN connection FAILED: {e}", 500
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)


