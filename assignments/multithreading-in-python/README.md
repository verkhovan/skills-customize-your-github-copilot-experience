# 📘 Assignment: Multithreading in Python

## 🎯 Objective

Learn how to run multiple tasks concurrently in Python using the `threading` module. In this assignment, you will create and manage threads, share data between them safely, and observe how concurrency speeds up real-world tasks.

## 📝 Tasks

### 🛠️ Create and Run Threads

#### Description
Use the `threading` module to create and start multiple threads that run functions concurrently.

#### Requirements
Completed program should:

- Import the `threading` module
- Define at least two functions that each print a series of messages (e.g. counting or logging)
- Create a `Thread` object for each function using `threading.Thread(target=...)`
- Start all threads with `.start()` and wait for them to finish with `.join()`
- Show that both functions execute concurrently (interleaved output is expected)


### 🛠️ Share Data Safely with a Lock

#### Description
Demonstrate a race condition when threads share a variable, then fix it using a `threading.Lock`.

#### Requirements
Completed program should:

- Define a shared counter variable accessible by multiple threads
- Create multiple threads that each increment the counter many times (e.g. 10,000 times each)
- First run the program **without** a lock and print the final counter value to show it may be incorrect
- Then protect the increment operation with a `threading.Lock` and print the correct final value
- Show the difference in results between the unprotected and protected versions


### 🛠️ Use a Thread Pool for Concurrent Tasks

#### Description
Use `concurrent.futures.ThreadPoolExecutor` to run a batch of tasks concurrently and collect their results.

#### Requirements
Completed program should:

- Define a function that simulates a slow task (e.g. squaring a number after a short `time.sleep`)
- Use `ThreadPoolExecutor` to submit at least 5 tasks concurrently
- Collect and print all results using `.result()` or `as_completed()`
- Print the total time taken and compare it to what sequential execution would take
