import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/version")
def version():
    return jsonify(version=os.getenv("APP_VERSION", "v1"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
