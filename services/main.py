import multiprocessing
from workers.gpt_worker import GPTWorker
from workers.worker import Worker
from task import Task
from db.sqlite_db import TaskDatabase
def run_worker_group(queue: multiprocessing.Queue, num_workers: int, WorkerClass: type[Worker]):
    workers = []
    for i in range(num_workers):
        worker_process = multiprocessing.Process(target=WorkerClass(queue, i).run)
        workers.append(worker_process)
        worker_process.start()
        
    for worker in workers:
        worker.join()

if __name__ == "__main__":
    db = TaskDatabase()
    task_queue = multiprocessing.Queue()
    worker = multiprocessing.Process(target=run_worker_group, args=(task_queue, 10, GPTWorker))
    worker.start()
    
    # Add a test task to the queue
    for i in range(100):
        task_queue.put(Task(id=f"test_task_{i}"))
    
    # Keep the main process running
    worker.join()