#Simple CLI To-Do List App

TASKS_FILE = "tasks.txt"
def load_tasks():
    try:
        with open(TASKS_FILE, "r")as file:
            tasks=[line.strip()for line in file.readlines()]
    except FileNotFoundError:
        tasks=[]
    return tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added.\n")
    else:
        print("No task entered.\n")
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
def main():
    tasks = load_tasks()
    while True:
        print("To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Thank you")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
