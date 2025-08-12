# app.py
from flask import Flask
import time
app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong blue", 200

@app.route("/")
def index():
    return "Hello, World! blue", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
