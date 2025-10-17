from utils import load_tasks

def add_task(task_name):
    tasks = load_tasks()
    # Check for duplicates (case-insensitive)
    if any(t['name'].lower() == task_name.lower() for t in tasks):
        print(f"Task '{task_name}' already exists.")
        return
    tasks.append({'name': task_name, 'done': False})
    # Removed save_tasks to introduce bug: changes not persisted
    print(f"Task '{task_name}' added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task['done'] else "Pending"
        # Bug: Indexing starts from 0, but user might expect 1
        print(f"{i}: {task['name']} - {status}")

def remove_task(index):
    tasks = load_tasks()
    # Bug: No validation for invalid index, will crash
    del tasks[index]
    # Removed save_tasks
    print("Task removed.")

def mark_done(index):
    tasks = load_tasks()
    # Bug: No validation for invalid index
    tasks[index]['done'] = True
    # Removed save_tasks
    print("Task marked as done.")
