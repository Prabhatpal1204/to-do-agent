from utils import load_tasks, save_tasks

def add_task(task_name):
    if not task_name.strip():
        print("Task name cannot be empty.")
        return
    tasks = load_tasks()
    # Check for duplicates (case-insensitive)
    if any(t['name'].lower() == task_name.lower() for t in tasks):
        print(f"Task '{task_name}' already exists.")
        return
    tasks.append({'name': task_name, 'done': False})
    save_tasks(tasks)
    print(f"Task '{task_name}' added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task['done'] else "Pending"
        print(f"{i+1}: {task['name']} - {status}")

def remove_task(index):
    tasks = load_tasks()
    index = index - 1  # Adjust for 1-based user input
    if index < 0 or index >= len(tasks):
        print("Invalid index.")
        return
    del tasks[index]
    save_tasks(tasks)
    print("Task removed.")

def mark_done(index):
    tasks = load_tasks()
    index = index - 1  # Adjust for 1-based user input
    if index < 0 or index >= len(tasks):
        print("Invalid index.")
        return
    tasks[index]['done'] = True
    save_tasks(tasks)
    print("Task marked as done.")
