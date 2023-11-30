from celery import Celery
import time
import subprocess
import os
import logging

app = Celery('myapp', broker='redis://localhost:6379/0',  backend='redis://localhost:6379/0')

@app.task
def say_hello():
    # Simulate a time-consuming operation (sleep for 10 seconds)
    #trigger_suit_cmd = ['pytest', '-v', '-s',  '--html', 'backgroundreport.html']
    os.chdir('/Users/deepakdas/InterviewKickStart/InterviewKickStart-1/leetcode/celery_flask/pytest')
    trigger_suit_cmd = ['pytest', '-v', '-s',  '--html', 'backgroundreport.html']
    process = subprocess.Popen(trigger_suit_cmd ,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    logging.info(f"pytest output:\n{stdout.decode('utf-8')}")
    time.sleep(30)
    
    # Return a placeholder message
    print("function is running")
    return "Hello, world! (Task completed)"