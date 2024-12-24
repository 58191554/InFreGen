import multiprocessing
from workers.worker import Worker
import time
class GPTWorker(Worker):
    """
    Worker that processes tasks using GPT.
    """
    def __init__(self, queue: multiprocessing.Queue, id: int):
        super().__init__(queue, id)

    def run(self):
        while True:
            task = self.queue.get()
            print(f"GPTWorker {self.id} received task {task.id}")
            time.sleep(1)
