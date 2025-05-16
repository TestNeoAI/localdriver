from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route("/run-test", methods=["GET"])
def run_test():
    try:
        result = subprocess.run(
            ["npx", "playwright", "test", "google-search.spec.js", "--headed"],
            capture_output=True,
            text=True
        )
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6081)
