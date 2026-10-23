from flask import Flask, jsonify
import socket

app = Flask(__name__)


def is_valid_port(port):
    return isinstance(port, int) and 1 <= port <= 65535


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/check/<int:port>")
def check(port):
    if not is_valid_port(port):
        return jsonify(error="invalid port"), 400
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        result = s.connect_ex(("127.0.0.1", port))
    return jsonify(port=port, open=(result == 0))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)