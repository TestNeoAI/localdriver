from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run-test', methods=['GET'])
def run_test():
    subprocess.Popen(["/bin/bash", "/run-tests.sh"])
    return "Playwright test started!", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6081)
