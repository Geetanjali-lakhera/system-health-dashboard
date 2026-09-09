import os
from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "1.0.0"
REQUEST_COUNT = 0


@app.before_request
def count_requests():
    global REQUEST_COUNT
    REQUEST_COUNT += 1


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": VERSION
    })


@app.route("/environment")
def environment():
    return jsonify({
        "environment": os.getenv("ENVIRONMENT", "development")
    })


@app.route("/status")
def status():
    return jsonify({
        "application": "system-health-dashboard",
        "status": "UP",
        "version": VERSION,
        "environment": os.getenv("ENVIRONMENT", "development")
    })


@app.route("/metrics")
def metrics():
    return jsonify({
        "service": "system-health-dashboard",
        "requests": REQUEST_COUNT
    })

@app.route("/info")
def info():
    return jsonify({
        "application": "system-health-dashboard",
        "description": "System health monitoring API"
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
