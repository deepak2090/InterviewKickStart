from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute_command')
def execute_command():
    command = 'python evenodd.py'

    # Run the command using subprocess.Popen and capture the output
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Read the output in real-time
    logs = []
    for line in process.stdout:
        logs.append(line.strip())

    # Wait for the process to complete
    process.wait()

    # Extract the output and return it as a JSON response
    output = '\n'.join(logs)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run()
