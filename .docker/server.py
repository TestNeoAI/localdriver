from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

# Allowed test files (hardcoded)
ALLOWED_TESTS = ["login_test.py", "signup_test.py"]

@app.route("/run-test", methods=["GET"])
def run_test():
    try:
        filename = request.args.get("file")
        if not filename:
            return jsonify({"error": "Missing 'file' parameter"}), 400

        if filename not in ALLOWED_TESTS:
            return jsonify({"error": f"Filename '{filename}' not supported"}), 400

        test_path = os.path.join("/tests", filename)
        if not os.path.isfile(test_path):
            return jsonify({"error": f"Test file '{filename}' not found on server"}), 404

        # Run the test using your shell script
        result = subprocess.run(
            ["bash", "/run-tests.sh", test_path],
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