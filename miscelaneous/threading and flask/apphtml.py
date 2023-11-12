from flask import Flask, render_template, request, jsonify
import time
import threading
import os
import subprocess

app = Flask(__name__)

done = False
worker_thread = None
start_time = time.time()

def worker():
    global done
    os.chdir("/Users/deepakdas/InterviewKickStart/InterviewKickStart-1/pytest")
    result = subprocess.Popen(["pytest", "-v", "-s"])
    result.wait()
    done = True

@app.route('/')
def index():
    return "hello flask"


@app.route('/start_counter')
def start_counter():
    global done, worker_thread

    #if worker_thread is None or not worker_thread.is_alive():
    done = False
    worker_thread = threading.Thread(target=worker)
    worker_thread.start()

    return jsonify({"message": "Process started please check reports after a while"})

if __name__ == '__main__':
    app.run(debug=True)
