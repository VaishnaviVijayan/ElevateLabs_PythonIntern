# Title: todo.py
# Author: Vaishnavi Vijayan
# Dis: A simple, clean and persistent To-Do List CLI app.

from colorama import Fore, Style, init
init(autoreset=True)

FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file; create file if not found."""
    try:
        with open(FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        open(FILE, "w").close()  # create empty file
        return []

def save_tasks(tasks):
    """Save the task list back into the file."""
    with open(FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display all tasks."""
    print(Fore.CYAN + "\n📌 Your To-Do List:")
    if not tasks:
        print(" (empty)")
    else:
        for i, task in enumerate(tasks, 1):
            print(f" {i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("➕ Enter task: ").strip()
    if task:
        tasks.append(task)
        print(Fore.GREEN + "Task added!")
    else:
        print(Fore.RED + "Cannot add empty task.")

def remove_task(tasks):
    """Remove a task by its number."""
    show_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("❌ Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(Fore.YELLOW + f"Removed: {removed}")
        else:
            print(Fore.RED + "Invalid task number.")
    except ValueError:
        print(Fore.RED + "Enter a valid number.")

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "\n✨ Vaishnavi's To-Do List App ✨")

    tasks = load_tasks()

    while True:
        print(Fore.LIGHTWHITE_EX + "\nChoose an option:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print(Fore.LIGHTGREEN_EX + "\nGoodbye! Your tasks are saved. 💚")
            break
        else:
            print(Fore.RED + "Invalid choice! Please select 1–4.")

if __name__ == "__main__":
    main()
