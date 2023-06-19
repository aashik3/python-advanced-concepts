import threading
import time

# Function to be executed by the daemon thread
def daemon_function():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_function)
daemon_thread.daemon = True

# Start the daemon thread
daemon_thread.start()

# Simulate some main thread operations
for i in range(1, 6):
    print(f"Main thread is running... Iteration {i}")
    time.sleep(2)

print("Main thread is done.")
