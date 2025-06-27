#!/bin/bash

echo "[+] Starting WireGuard..."
wg-quick up wg0

echo "[+] Starting Flask API via gunicorn..."
gunicorn -b 0.0.0.0:10000 app:app
