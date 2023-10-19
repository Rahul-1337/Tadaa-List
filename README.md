# Tadaa List (To-do list)

#### Video Demo: https://youtu.be/OcL-3LskmAg

#### Description:
The To-Do List Application is a simple command-line tool designed to help users manage their daily tasks. It provides basic functionality to add tasks, remove tasks, and view the list of tasks. This project serves as a beginner-level Python project that demonstrates fundamental concepts such as functions, lists, user input handling, and basic testing using pytest.

## Features:
- **Add Task**: Users can add tasks to the to-do list.
- **Remove Task**: Users can remove tasks from the list by specifying the task to be removed.
- **View Tasks**: Users can view all tasks currently in the to-do list.
- **Error Handling**: The application provides error handling for cases where users try to remove a task that doesn't exist.

## Usage

1. Run the program.
2. You will be presented with a menu of options: Add task (A), Remove task (R), View tasks (V), and Quit (Q).
3. Depending on your choice, you can perform the following actions:

    - **Add task (A)**: You can add a task by entering a description when prompted. The task will be added to the list of tasks.

    - **Remove task (R)**: If there are tasks in the list, you can remove a task by entering the number corresponding to the task you want to remove. The program will validate the input and remove the task at the specified index.

    - **View tasks (V)**: You can view the current list of tasks. If there are no tasks, it will indicate that there are no tasks yet.

    - **Quit (Q)**: You can quit the program at any time.

## Code Explanation

The code is structured as follows:

- An empty list called `tasks` is initialized to store the tasks.
- The `main()` function is the entry point of the program. It displays the menu, accepts user input, and calls corresponding functions based on the user's choice.
- There are three main functions used in the program:
    - `add_task(task)`: Adds a task to the `tasks` list.
    - `remove_task_by_index(index)`: Removes a task from the `tasks` list by index.
    - `view_tasks()`: Returns the list of tasks.
- Error handling is implemented to ensure valid user input.
- The program runs in a loop until the user chooses to quit.

## Example Usage

```python
This is a very simple To-do-list!

Options:

A. Add task
R. Remove task
V. View tasks
Q. Quit
Enter your choice: A
Enter the task: Buy groceries

Options:

A. Add task
R. Remove task
V. View tasks
Q. Quit
Enter your choice: A
Enter the task: Pay bills

Options:

A. Add task
R. Remove task
V. View tasks
Q. Quit
Enter your choice: V
Tasks:
1. Buy groceries
2. Pay bills

Options:

A. Add task
R. Remove task
V. View tasks
Q. Quit
Enter your choice: R
Tasks:
1. Buy groceries
2. Pay bills
Enter the number of the task to remove: 1

Options:

A. Add task
R. Remove task
V. View tasks
Q. Quit
Enter your choice: V
Tasks:
1. Pay bills

Options:

A. Add task
R. Remove task
V. View tasks
Q. Quit
Enter your choice: Q
At your service, always!
```

## Demo Video:
You can watch a demonstration of the To-Do List Application in action by clicking on the following link: https://youtu.be/OcL-3LskmAg

## Project Structure:
- `project.py`: Contains the main code for the to-do list application.
- `test_project.py`: Includes test cases for the functions in `project.py`.

Feel free to use and customize this basic to-do list application for your own task management needs or as a starting point for further Python development projects.

Enjoy staying organized with your to-do list!







