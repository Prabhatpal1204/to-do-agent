from task_manager import add_task, list_tasks, remove_task, mark_done

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. List tasks")
        print("3. Remove task")
        print("4. Mark task as done")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task_name = input("Enter task name: ")
            # Bug: No validation for empty task name
            add_task(task_name)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            index = int(input("Enter task index to remove: "))
            # Bug: Assumes input is int, crashes otherwise
            remove_task(index)
        elif choice == '4':
            index = int(input("Enter task index to mark done: "))
            # Bug: Assumes input is int
            mark_done(index)
        elif choice == '5':
            # Bug: Doesn't save tasks on exit
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
