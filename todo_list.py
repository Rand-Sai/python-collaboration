#Project Task: Write a Python program that simulates a simple "To-Do List". The program should allow users to:
# Add new tasks.
# View all tasks.
# Mark tasks as completed.
# Delete tasks.

# Dictionary to store taks
task_dict = {"Task Name": ("Description", "Status")}

# Add Function
def add(data_dict):
    task_name = input("What's the name of the task: \n")
    task_info = input("Provide description of the task: \n")
    while 1:
        task_status = input("Is the task complete? Enter Y for yes; Enter N for no. \n")
        if task_status.upper() == "Y":
            task_status = "Complete"
            break
        elif task_status.upper() == "N":
            task_status = "Incomplete"
            break
        else:
            print("Error. You have entered something other than Y/N, please try again. \n")
    data_dict[task_name] = (task_info, task_status)

    print("Task " + task_name + " added.")

# View Task
def view(data_dict):
    for key, value in data_dict.items():
        print(f"{key}: {value} \n")

# Mark Task
def mark(data_dict):
    for key, value in data_dict.items():
        print(f"{key}: {value} \n")
    task = input("Which task do you want to mark as complete? \n")
    while 1:
        if task in data_dict.keys():
            task_info = list(data_dict[task])
            task_info[1] = "Complete"
            data_dict[task] = tuple(task_info)
            print("Task " + task + " marked as complete. \n")
            break
        else:
            print("The task you enter does not exist. Please enter the full name of the task. \n")

# Delete Task
def delete(data_dict):
    for key, value in data_dict.items():
        print(f"{key}: {value}")
    task = input("Which task do you want to delete? \n")
    while 1:
        if task in data_dict.keys():
            del data_dict[task]
            print("Task " + task + " deleted. \n")
            break
        else:
            print("The task you enter does not exist. Please enter the full name of the task. \n")

#Sort Tasks
def sort_tasks(data_dict):
    print("How would you like to sort the tasks?\n")
    print("(1) By Name")
    print("(2) By Status")
    sort_by = input("Choose an option (1 or 2): ")

    if sort_by == "1":
        # Sort by task name
        sorted_by_name = sorted(data_dict.items(), key=lambda x: x[0].lower())
        print("Tasks sorted by Name:")
    elif sort_by == "2":
        # Sort by status
        sorted_by_name = sorted(data_dict.items(), key=lambda x: (x[1][1] != "Incomplete", x[0].lower()))
        print("Tasks sorted by Status (Incomplete first):")
    else:
        print("Invalid option. Returning to main menu.")
        return

    for task, details in sorted_by_name:
        print(f"{task}: Description: {details[0]}, Status: {details[1]}")


# Save Tasks
def save_to_file(data_dict):
    file_name = input("Enter the filename to save tasks (e.g., tasks.txt): \n")
    with open(file_name, 'w') as file:
        for task_name, (description, status) in data_dict.items():
            file.write(f"{task_name}|{description}|{status}\n")
    print(f"Tasks saved to {file_name}")

# Main Program
def main():
    print("Hello! \n")
    print("Welcome to the Task Program. \n")

    while 1:
        print("Select action: Add Task(1) | View Task(2) | Mark as Complete(3) | Delete Task(4) | Sort Task(5) | Save Task(6) | Exit(7) \n")
        choice = (input("Enter the number corresponding to the action you want to take: \n"))
        if choice == "1":
            add(task_dict)
        elif choice == "2":
            view(task_dict)
        elif choice == "3":
            mark(task_dict)
        elif choice == "4":
            delete(task_dict)
        elif choice == "5":
            sort_tasks(task_dict)
        elif choice == "6":
            save_to_file(task_dict)
        elif choice == "7":
            print("Exitng program... \n")
            break
        else:
            print("Error. Number not recongized. Please try agian. \n")

main()