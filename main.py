import subprocess
import time
from threading import Thread
from flask import Flask

app = Flask(__name__)

@app.route("/")
def run():
    return {"message": "success"}

def run_flask():
    app.run(host="127.0.0.1", port=8080)

def run_socat():
    subprocess.run(['socat', 'TCP-LISTEN:80,fork', 'TCP:127.0.0.1:8080'])

if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    time.sleep(2)
    run_socat()
