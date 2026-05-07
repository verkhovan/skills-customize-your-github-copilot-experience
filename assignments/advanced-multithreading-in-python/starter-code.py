# Starter Code: Advanced Multithreading in Python

import queue
import threading
import time


# --- Shared resources ---
job_queue = queue.Queue()
metrics = {
    "processed_count": 0,
    "error_count": 0,
    "total_duration": 0.0,
}
metrics_lock = threading.Lock()
stop_event = threading.Event()


# --- Task 1: Build a Producer-Consumer Pipeline ---

def producer(name, num_jobs):
    """Create jobs and place them in the shared queue."""
    # TODO: push num_jobs jobs into job_queue
    # Suggested job format: {"id": f"{name}-{i}", "payload": i}
    pass


def consumer(name):
    """Continuously consume jobs until shutdown is requested."""
    # TODO: Loop until stop_event is set and queue is drained
    # TODO: Get jobs with a timeout so you can re-check stop_event
    # TODO: Handle sentinel (None) jobs for graceful shutdown
    # TODO: Call process_job(job) and then job_queue.task_done()
    pass


# --- Task 2: Protect Shared State and Collect Metrics ---

def process_job(job):
    """Simulate work and update shared metrics safely."""
    # TODO: Record start time
    # TODO: Simulate variable work, for example: time.sleep(0.05 + job["payload"] * 0.01)
    # TODO: Update processed_count and total_duration inside metrics_lock
    # TODO: If an exception occurs, increment error_count safely
    pass


def print_metrics_summary():
    """Print final metrics, including average time per processed job."""
    # TODO: Read values safely and compute average time
    # TODO: Print processed_count, error_count, total_duration, and average
    pass


# --- Task 3: Implement Graceful Shutdown with Event Signals ---

def main():
    producers = []
    consumers = []

    # TODO: Start 2 producers
    # TODO: Start 3 consumers

    # TODO: Wait for all producers to finish
    # TODO: Wait for all jobs to be processed with job_queue.join()

    # Option A: Put one sentinel (None) per consumer
    # Option B: Set stop_event and let consumers exit when queue is empty

    # TODO: Signal shutdown and join all consumers
    # TODO: Print final metrics summary
    pass


if __name__ == "__main__":
    main()
