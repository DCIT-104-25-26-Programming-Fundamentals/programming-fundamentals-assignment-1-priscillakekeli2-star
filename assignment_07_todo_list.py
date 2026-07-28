# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# Console-Based To-Do List Application
# =============================================================================

# List to store tasks
tasks = []


# Function to add a task
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


# Function to view all tasks
def view_tasks():
    if not tasks:
        print("Your task list is empty.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


# Function to delete a task
def delete_task():
    if not tasks:
        print("There are no tasks to delete.")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main program loop
while True:
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")