"""Simple console To-Do app (fixed style).
This app allows users to add, show, and remove tasks from a list.
"""

tasks = []  # global task list


def add_task(task):
    """Add a non-empty task to the list."""
    if task:  # check if task is not empty
        tasks.append(task)
        print(f'Task "{task}" added.')
    else:
        print("Cannot add an empty task.")


def show_tasks():
    """Display all current tasks with numbering."""
    if not tasks:
        print("No tasks to show.")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


def remove_task(task_number):
    """Remove a task from the list by its number."""
    try:
        index = task_number - 1  # convert to 0-based index
        removed = tasks.pop(index)
        print(f'Task "{removed}" removed.')
    except (IndexError, ValueError):
        print("Invalid task number.")


def main():
    """Run the main loop for the To-Do app."""
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
