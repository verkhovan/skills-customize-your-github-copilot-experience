# 📘 Assignment: Advanced Multithreading in Python

## 🎯 Objective

Apply advanced multithreading patterns in Python to coordinate worker threads, process shared data safely, and shut down background work gracefully. By the end, you will build a small threaded processing pipeline that is reliable and easy to debug.

## 📝 Tasks

### 🛠️ Build a Producer-Consumer Pipeline

#### Description
Create a producer-consumer system where one or more producer threads generate jobs and worker threads process them using a shared queue.

#### Requirements
Completed program should:

- Use `queue.Queue` for thread-safe job handoff between producers and consumers
- Start at least 2 producer threads and 3 consumer threads
- Have each producer create multiple jobs (for example, dictionaries with an `id` and `payload`)
- Have each consumer fetch jobs with `.get()`, process them, and call `.task_done()`
- Wait for all queued jobs to finish with `.join()`


### 🛠️ Protect Shared State and Collect Metrics

#### Description
Track pipeline metrics (like total processed jobs and total processing time) while multiple threads update the same shared state.

#### Requirements
Completed program should:

- Keep shared metrics in a dictionary or class (for example, `processed_count`, `error_count`, `total_duration`)
- Use `threading.Lock` or `threading.RLock` around all writes to shared metrics
- Simulate variable processing time with `time.sleep()`
- Print a final metrics summary after all jobs complete
- Include at least one computed value, such as average time per job


### 🛠️ Implement Graceful Shutdown with Event Signals

#### Description
Add a clean shutdown flow so workers can stop safely after processing all jobs or when a stop signal is sent.

#### Requirements
Completed program should:

- Create a shared `threading.Event` (for example, `stop_event`) to signal shutdown
- Make worker threads periodically check the event and exit cleanly
- Use a sentinel value (for example, `None`) or event-based logic to stop consumers
- Join all threads before exiting the program
- Print clear start/stop log messages for each worker so thread lifecycle is visible
