# Task Manager CLI Application

A simple command-line task management application that allows users to add, view, update and delete tasks with deadlines and priorities.

## Features

- Add new tasks with title, deadline, and priority
- View all tasks with their details
- Mark tasks as complete
- Delete tasks
- Persistent storage using tasks.txt file
- Simple text-based interface

## Installation

```bash
git clone https://github.com/yourusername/task-manager.git
```

## Usage

1. Run the application:
```bash
python task_manager.py
```

2. Select options from the menu:
- 1. Add Task
- 2. View Tasks
- 3. Mark Task as Complete
- 4. Delete Task
- 5. Exit

## File Format

Tasks are stored in `tasks.txt` with the following format:
```
1 | Task Title | incomplete | 2023-12-31 | medium
2 | Review project | complete | 2023-10-15 | high
```

## License

MIT
