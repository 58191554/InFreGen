import multiprocessing
from workers.worker import Worker
from task import Task
class DatabaseWorker(Worker):
    """
    Worker that processes tasks using the database.
    """
    def __init__(self, queue: multiprocessing.Queue, id: int):
        super().__init__(queue, id)

    def run(self):
        while True:
            task = self.queue.get()
            # task can be put or get
        
    def put(self, task: Task):
        # TODO: put task into database
        pass
        
    def get(self):
        # TODO: get task from database
        pass