# Starter Code: Multithreading in Python

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# --- Task 1: Create and Run Threads ---

# TODO: Define a function `print_numbers(name, count)` that prints
#       "{name}: {i}" for i in range(count), with a short time.sleep between prints

# TODO: Create two Thread objects targeting print_numbers with different names
# TODO: Start both threads and join them
# TODO: Print a message after both threads finish


# --- Task 2: Share Data Safely with a Lock ---

counter = 0  # Shared variable

# TODO: Define a function `increment(n)` that increments `counter` n times
#       (without a lock first, to demonstrate the race condition)

# TODO: Create 5 threads each calling increment(10_000)
# TODO: Start and join all threads, then print the final counter value
#       (it will likely be less than 50,000 — that's the race condition)

# TODO: Reset counter to 0, create a Lock, and rewrite increment to use it
# TODO: Repeat with 5 threads and print the correct final value (should be 50,000)


# --- Task 3: Thread Pool for Concurrent Tasks ---

# TODO: Define a function `slow_task(n)` that sleeps for 1 second and returns n ** 2

# TODO: Record the start time using time.time()
# TODO: Use ThreadPoolExecutor(max_workers=5) to submit slow_task for n in range(5)
# TODO: Collect results as they complete using as_completed() and print each one
# TODO: Print total elapsed time and note how it compares to 5 seconds sequential
