from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

# ID único da instância baseado no hostname do container
INSTANCE_ID = os.environ.get("INSTANCE_ID", socket.gethostname())

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "instance": INSTANCE_ID}), 200

@app.route('/api/info')
def info():
    return jsonify({
        "message": "TechNova API - E-commerce",
        "instance_id": INSTANCE_ID,
        "load_simulation": "OK"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)