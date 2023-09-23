from flask import Flask, render_template, Response, jsonify
import subprocess
import json
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/execute_command')
def execute_command():
    def generate():
        command = 'python evenodd.py'
        time.sleep(5)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Read the output in real-time and send progress updates
        for line in process.stdout:
            yield f"data: {json.dumps({'progress': 'Executing...'})}\n\n"
            yield f"data: {json.dumps({'output': line.strip()})}\n\n"

        # Wait for the process to complete
        process.wait()

        # Send final completion message and result
        yield f"data: {json.dumps({'progress': 'Execution complete.'})}\n\n"
        yield f"data: {json.dumps({'output': 'Execution complete.'})}\n\n"
        yield "event: close\ndata: Task Complete\n\n"

    return Response(generate(), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)