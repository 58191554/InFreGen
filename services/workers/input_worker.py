import multiprocessing
from workers.worker import Worker
import time
class InputWorker(Worker):
    """
    Worker that initialize the task with input description
    store the task in the database
    """
    def __init__(self, queue: multiprocessing.Queue, id: int, db):
        super().__init__(queue, id)

    def run(self):
        while True:
            task = self.queue.get()
            print(f"GPTWorker {self.id} received task {task.id}")
            time.sleep(1)
