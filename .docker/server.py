from flask import Flask
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # 👈 This line enables CORS for all domains

@app.route('/run-test', methods=['GET'])
def run_test():
    subprocess.Popen(["/bin/bash", "/run-tests.sh"])
    return "Playwright test started!", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6081)
