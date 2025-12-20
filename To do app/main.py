from todo_manager import TodoManager

def menu():
    print("\n My Todo App ")
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Update Todo")
    print("4. Delete Todo")
    print("5. Exit")

def main():
    manager = TodoManager()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter a task: ")
            manager.add_task(title)
            print("You added a task successfully.")

        elif choice == "2":
            manager.view_tasks()


        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            new_title = input("New title : ")
            completed_input = input("Mark as completed? (y/n/skip): ")

            completed = None
            if completed_input.lower() == "y":
                completed = True
            elif completed_input.lower() == "n":
                completed = False

            success = manager.update_task(
                task_id,
                new_title if new_title else None,
                completed
            )

            if success:
                print("Todo updated successfully.")
            else:
                print("Todo not found.")

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            manager.delete_task(task_id)
            print("Todo deleted.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
