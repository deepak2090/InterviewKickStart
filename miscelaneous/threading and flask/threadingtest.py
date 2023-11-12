import time
import threading

done = False

def worker():
    counter = 0
    while not done:
        time.sleep(0.6)
        counter += 1
        print(counter)

# Start the worker thread
worker_thread = threading.Thread(target=worker)
worker_thread.start()
print("program is complete")

try:
    input("Press Enter to stop the counter")
except KeyboardInterrupt:
    # Handle Ctrl+C (keyboard interrupt)
    pass

done = True  # Set the flag to stop the worker thread
worker_thread.join()  # Wait for the worker thread to complete
