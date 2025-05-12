from flask import Flask
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/run-test', methods=['GET'])
def run_test():
    os.environ["DISPLAY"] = ":1"
    result = subprocess.run(["/run-tests.sh"], capture_output=True, text=True)
    return result.stdout + result.stderr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6081)
