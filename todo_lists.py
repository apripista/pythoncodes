# To-Do List Application
tasks = []


def add_task(task):
    tasks.append({'task': task, 'complete': False})


def view_tasks():
    for idx, task in enumerate(tasks, start=1):
        status = '✓' if task['complete'] else ' '
        print(f"{idx}. [{status}] {task['task']}")


def mark_complete(task_idx):
    if 0 < task_idx <= len(tasks):
        tasks[task_idx - 1]['complete'] = True
        print("Task marked as complete.")
    else:
        print("Invalid task index.")


def save_tasks(filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']},{task['complete']}\n")


def load_tasks(filename):
    tasks.clear()
    try:
        with open(filename, 'r') as file:
            for line in file:
                task, complete = line.strip().split(',')
                tasks.append({'task': task, 'complete': complete == 'True'})
    except FileNotFoundError:
        pass


def main():
    load_tasks('tasks.txt')
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            task_idx = int(input("Enter the task number to mark as complete: "))
            mark_complete(task_idx)
        elif choice == '4':
            save_tasks('tasks.txt')
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
