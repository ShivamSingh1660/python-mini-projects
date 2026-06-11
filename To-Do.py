task = []

def ADD():
    x = input("Enter your task: ")
    task.append(x)
    print("Task Added Successfully!")

def Delete():
    if len(task) == 0:
        print("Task List is Empty!")
        return

    View()

    x = int(input("Enter task number to delete: "))

    if 1 <= x <= len(task):
        removed = task.pop(x - 1)
        print(f"'{removed}' deleted successfully!")
    else:
        print("Invalid task number!")

def View():
    if len(task) == 0:
        print("No Tasks Available!")
    else:
        print("\nTasks:")
        for i in range(len(task)):
            print(f"{i+1}. {task[i]}")
        print()

while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ADD()

    elif choice == 2:
        Delete()

    elif choice == 3:
        View()

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")