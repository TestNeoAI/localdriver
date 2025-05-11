from flask import Flask
from flask_cors import CORS
import subprocess
import os
app = Flask(__name__)
CORS(app)  # Enables CORS for all routes



@app.route('/run-test', methods=['GET'])
def run_test():
    import os
    env = os.environ.copy()
    env["DISPLAY"] = ":1"
    subprocess.Popen(["/bin/bash", "/run-tests.sh"], env=env)
    return "Playwright test started!", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6081)
