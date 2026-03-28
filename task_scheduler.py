class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n=== Task Scheduler Menu ===")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Run First-Come-First-Serve (FCFS) scheduling")
        print("4. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks yet. Add your first task!")
            return
        print("\nCurrent Tasks:")
        print("Name\tArrival Time")
        for t in self.tasks:
            print(f"{t['name']}\t{t['arrival']}")

    def add_task(self, name, arrival):
        self.tasks.append({"name": name, "arrival": arrival})
        print("Task added.")

    def fcfs_schedule(self):
        if not self.tasks:
            print("No tasks to schedule.")
            return
        # Sort tasks by arrival time
        sorted_tasks = sorted(self.tasks, key=lambda x: x['arrival'])
        
        print("\nFCFS Schedule (Order of Execution):")
        for i, task in enumerate(sorted_tasks, start=1):
            print(f"{i}. {task['name']} (Arrives at {task['arrival']})")


def main():
    scheduler = TaskScheduler()
    while True:
        scheduler.display_menu()
        choice = input("Select an option (1-4): ").strip()
        if choice == '1':
            scheduler.view_tasks()
        elif choice == '2':
            name = input("Enter task name: ").strip()
            if not name:
                print("Task name cannot be empty.")
                continue
            try:
                arrival = int(input("Enter arrival time: "))
                scheduler.add_task(name, arrival)
            except ValueError:
                print("Please enter a valid number for arrival time.")
        elif choice == '3':
            scheduler.fcfs_schedule()
        elif choice == '4':
            print("Exiting the Task Scheduler. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()