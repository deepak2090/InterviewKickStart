from re import sub
import subprocess
import os
os.chdir('/Users/deepakdas/InterviewKickStart/InterviewKickStart-1/pytest')

process = subprocess.Popen(["pytest","-v","-s"])
message1 = "the process is running in the background"
print(message1)

import time
time.sleep(5)
if process.poll() is None:
    
    message2 = "the process is still running"
else:
    message2 = "the proess has finished"

print(message2)