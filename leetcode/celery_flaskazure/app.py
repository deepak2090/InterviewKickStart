
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello')
def hello():
    # Trigger the Celery task to say hello
    return "hello deepak"


if __name__ == '__main__':
    app.run(debug=True, StreamRecoder = True)