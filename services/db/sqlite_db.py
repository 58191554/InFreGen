from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
import json
import random

# Define the base class for the ORM
Base = declarative_base()

# Define an Enum for the state field
class TaskState(enum.Enum):
    INPUT = "INPUT"
    GPT = "GPT"
    OUTPUT = "OUTPUT"

# Define the Task table
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    path = Column(String, nullable=False)
    state = Column(Enum(TaskState), nullable=False)

    def __repr__(self):
        return f"<Task(id={self.id}, description={self.description}, path={self.path}, state={self.state})>"

# Encapsulate the database operations in a class
class TaskDatabase:
    def __init__(self, database_url="sqlite:///tasks.db", config=None):
        # Create the database engine
        self.engine = create_engine(database_url)
        # Create all tables if they do not exist
        Base.metadata.create_all(self.engine)
        # Create a session factory
        self.Session = sessionmaker(bind=self.engine)

    def add_task(self, new_task: Task):
        """Add a new task to the database."""
        with self.Session() as session:
            session.add(new_task)
            session.commit()
            return new_task

    def update_task(self, task_id, description=None, path=None, state=None):
        """Update an existing task."""
        with self.Session() as session:
            task = session.query(Task).filter(Task.id == task_id).one_or_none()
            if not task:
                raise ValueError(f"Task with id {task_id} not found.")
            if description is not None:
                task.description = description
            if path is not None:
                task.path = path
            if state is not None:
                task.state = state
            session.commit()
            return task

    def delete_task(self, task_id):
        """Delete a task from the database."""
        with self.Session() as session:
            task = session.query(Task).filter(Task.id == task_id).one_or_none()
            if not task:
                raise ValueError(f"Task with id {task_id} not found.")
            session.delete(task)
            session.commit()

    def get_tasks(self):
        """Retrieve all tasks."""
        with self.Session() as session:
            return session.query(Task).all()

    def get_task_by_id(self, task_id):
        """Retrieve a task by its ID."""
        with self.Session() as session:
            return session.query(Task).filter(Task.id == task_id).one_or_none()

# Example usage
if __name__ == "__main__":
    db = TaskDatabase()

    # Add a new task
    new_task = Task(description="Example task", path="/path/to/resource", state=TaskState.INPUT)
    task = db.add_task(new_task)

    # # Retrieve and print all tasks
    # tasks = db.get_tasks()
    # print(tasks)

    # # Update a task
    # updated_task = db.update_task(task_id=2, state=TaskState.GPT)

    # # Delete a task
    # db.delete_task(task_id=1)
    
    task = db.get_task_by_id(task_id=2)
    print(type(task))
    print(task)
    print(task.description)
