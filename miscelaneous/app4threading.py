from flask import Flask
from flask_restful import Resource, Api
import time
import threading
 
 
app = Flask(__name__)
api = Api(app)
 
 
def task():
 
    """
    background Process handled by Threads
    :return: None
    """
 
    print("Started Task ...")
    print(threading.current_thread().name)
    time.sleep(6)
    
    print("completed .....")
 
 
class HelloWorld(Resource):
    def get(self):
        #threading.Thread(target=task).start()
        task()
        return {'hello': 'world'}
 
 
api.add_resource(HelloWorld, '/')
 
 
 
if __name__ == '__main__':
    app.run(debug=True)