from celery import Celery
import time

app = Celery('myapp', broker='redis://localhost:6379/0',  backend='redis://localhost:6379/0')

@app.task
def say_hello():
    # Simulate a time-consuming operation (sleep for 10 seconds)
    time.sleep(30)
    
    # Return a placeholder message
    print("function is running")
    return "Hello, world! (Task completed)"
