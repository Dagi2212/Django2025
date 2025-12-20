import json
import os
from task import Task

class TodoManager:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
      try:
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        else:
            with open(self.filename, "w") as file:
                json.dump([], file)
      except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")
        self.tasks = []


    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        self.tasks.append(Task(task_id, title))
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No todos found.")
            return
        for task in self.tasks:
            status = "✔ Completed" if task.completed else "❌ Not Completed"
            print(f"{task.id}. {task.title} - {status}")

    def update_task(self, task_id, new_title=None, completed=None):
        for task in self.tasks:
            if task.id == task_id:
                if new_title:
                    task.title = new_title
                if completed is not None:
                    task.completed = completed
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        for index, task in enumerate(self.tasks):
            task.id = index + 1
        self.save_tasks()
