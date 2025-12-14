#The task is to create a task list for a shark week theme event.
#Party task list manager
#Simple task list manager tool for organizing a shark week themed event 

class PartyTaskList:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n=== Party Task List Menu ===")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks yet. Add your first party task!")
            return
        print("\nCurrent Party Tasks:")
        for i, t in enumerate(self.tasks, start=1):
            status = "Done" if t["done"] else "Pending"
            print(f"{i}. {t['task']} - {status}")

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print("Task added.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")


def main():
    task_list = PartyTaskList()
    while True:
        task_list.display_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            task_list.view_tasks()
        elif choice == '2':
            task = input("Enter the new task: ")
            if task.strip() == "":
                print("Task cannot be empty.")
            else:
                task_list.add_task(task)
        elif choice == '3':
            try:
                index = int(input("Enter the task number to mark as completed: ")) - 1
                task_list.mark_task_completed(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                task_list.remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the Party Task List Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()