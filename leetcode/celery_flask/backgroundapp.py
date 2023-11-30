from flask import Flask, jsonify
from celery import Celery
from tasks import say_hello
app = Flask(__name__)

# Configure Celery with a message broker (e.g., Redis, RabbitMQ)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Create a Celery instance
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/hello/<i>')
def hello(i):
    # Trigger the Celery task to say hello
    result = say_hello.apply_async()

    # Return an immediate response to the client with the task ID
    response = {
        "message": f"Saying new hello in the background. Check back later for results. {i}",
        "task_id": result.id
    }
    return jsonify(response)

@app.route('/get_result/<task_id>')
def get_result(task_id):
    # Check the status and result of the Celery task
    result = say_hello.AsyncResult(task_id)

    if result.state == 'SUCCESS':
        # The task has completed successfully
        response = {
            "message": "Task completed successfully",
            "result": result.result,
        }
    elif result.state == 'FAILURE':
        # The task has failed
        response = {
            "message": "Task failed",
            "result": str(result.result),  # Include error message
        }
    else:
        # The task is still in progress
        response = {
            "message": "Task is still in progress",
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run()