tasks = []

def main():
    print("This is a bhery simple To-do-list!\n")

    while True:
        print("Options:\n")
        print("A. Add task")
        print("R. Remove task")
        print("V. View tasks")
        print("Q. Quit")

        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == 'R':
            tasks_list = view_tasks()
            if len(tasks_list) == 0:
                print("There are no tasks yet.")
            else:
                print("Tasks:")
                for index, task in enumerate(tasks_list, start=1):
                    print(f"{index}. {task}")
                task_number = input("Enter the number of the task to remove: ")
                try:
                    task_number = int(task_number)
                    if 1 <= task_number <= len(tasks_list):
                        remove_task_by_number(task_number - 1)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == 'V':
            tasks_list = view_tasks()
            if len(tasks_list) == 0:
                print("There are no tasks yet.")
            else:
                print("Tasks:")
                for index, task in enumerate(tasks_list, start=1):
                    print(f"{index}. {task}")
        elif choice == 'Q':
            print("This was Tadaa list!")
            break
        else:
            print("Invalid choice. Try something from 'A', 'R', 'V', 'Q'\n")


def add_task(task):
    # Add a task to the to-do list
    tasks.append(task)

def remove_task_by_number(index):
    # Remove a task from the to-do list by index
    if 0 <= index < len(tasks):
        del tasks[index]
    else:
        print("Invalid task index.")

def view_tasks():
    # View all tasks in the to-do list
    return list(tasks)

if __name__ == "__main__":
    main()
