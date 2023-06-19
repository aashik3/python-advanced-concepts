import time

# Get the current time in seconds since the epoch
current_time = time.time()
print("Current time:", current_time)

# Sleep for 2 seconds
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake!")

# Convert seconds since the epoch to a struct_time object
local_time = time.localtime(current_time)
print("Local time:", local_time)

# Format the local time as a string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted time:", formatted_time)

# Measure the execution time of a code block
start_time = time.time()
# Code block to measure execution time
for i in range(1000000):
    pass
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")

# Convert a string representing a time to seconds since the epoch
time_string = "2023-06-18 10:30:00"
time_struct = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
time_seconds = time.mktime(time_struct)
print("Time in seconds since the epoch:", time_seconds)

# Get the CPU time in seconds
cpu_time = time.process_time()
print("CPU time:", cpu_time)
