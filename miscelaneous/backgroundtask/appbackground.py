from time import sleep
from flask import Flask
#from flask_cors import CORS
import threading
app = Flask(__name__)

thread_event = threading.Event()


def backgroundTask(number):
    
    while thread_event.is_set() and i < number:
        print('Background task running!')
        for i in range(1,number):
            print(i)
            i+=1


@app.route("/start/<number>", methods=["POST","GET"])
def startBackgroundTask(number):
    try:
        thread_event.set()
        number = int(number)
        
        thread = threading.Thread(target=backgroundTask, args = (number,))
        thread.start()

        return "Background task started!"
    except Exception as error:
        return str(error)

@app.route("/stop", methods=["POST","GET"])
def stopBackgroundTask():
    try:
        thread_event.clear()

        return "Background task stopped!"
    except Exception as error:
        return str(error)