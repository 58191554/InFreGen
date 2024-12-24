import multiprocessing
import time

class Worker:
    """
    Base class for all workers. Other workers should inherit from this class.
    """
    def __init__(self, queue: multiprocessing.Queue, id: int):
        self.queue = queue
        self.id = id
        print(f"Worker {self.id} initialized")

    def run(self):
        while True:
            task = self.queue.get()
            print(f"Worker {self.id} received task {task.id}")
            time.sleep(1)
