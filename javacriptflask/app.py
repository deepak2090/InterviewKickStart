from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Sample resources
@app.route('/x', methods=['GET'])
def resource_x():
    time.sleep(10)  # Simulating a delay
    return jsonify({'result': 'Resource X response'})

@app.route('/y', methods=['POST'])
def resource_y():
    time.sleep(3)  # Simulating a delay
    return jsonify({'result': 'Resource Y response'})

@app.route('/z', methods=['POST'])
def resource_z():
    time.sleep(4)  # Simulating a delay
    return jsonify({'result': 'Resource Z response'})

# Main route with the form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_resource = request.form.get('resource')
        # Assuming you have JavaScript logic to handle the response asynchronously
        javascript_response = f"alert('Received response from {selected_resource}');"
        return render_template('index.html', javascript_response=javascript_response)
    return render_template('index.html', javascript_response=None)

if __name__ == '__main__':
    app.run(debug=True)
