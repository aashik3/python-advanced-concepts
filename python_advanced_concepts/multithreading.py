import threading
import time

# Function to be executed by each thread
def thread_function(name, delay):
    print("Thread", name, "started.")

    # Perform some computation
    for i in range(5):
        print("Thread", name, "computing...")
        time.sleep(delay)

    # Acquire a lock and update a shared variable
    lock.acquire()
    shared_variable[0] += 1
    lock.release()

    # Perform I/O operation
    print("Thread", name, "writing to file...")
    with open("output.txt", "a") as file:
        file.write(f"Thread {name} wrote to file.\n")

    print("Thread", name, "finished.")

# Create a lock object
lock = threading.Lock()

# Create a shared variable
shared_variable = [0]

# Create and start multiple threads
threads = []
for i in range(1, 4):
    thread = threading.Thread(target=thread_function, args=(f"Thread-{i}", i))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads finished.")
print("Shared variable value:", shared_variable[0])
