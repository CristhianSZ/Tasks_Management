
import os
FILE_NAME = "tasks.txt"
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                if line.strip():
                    task_id, title, status, deadline, priority = line.strip().split(" | ")
                    tasks[int(task_id)] = {"title": title, "status": status, "deadline": deadline, "priority": priority}
    return tasks




def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        for task_id, task in tasks.items():
            file.write(
                f"{task_id} | {task['title']} | {task['status']} | {task['deadline']} | {task['priority']}\n")


def add_task(tasks):
    title = input("Enter task title: ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    priority = input("Enter task priority (low/medium/high): ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete", "deadline": deadline, "priority": priority}
    print(f"Task added with ID: {task_id}")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(
                f"ID: {task_id}, Title: {task['title']}, Status: {task['status']} , Deadline: {task['deadline']}, Priority: {task['priority']}")


def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]['status'] = 'complete'
        print(f"Task ID {task_id} marked as complete.")
    else:
        print("Task ID not found.")


def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task ID {deleted_task} deleted.")
    else:
        print("Task ID not found.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()


