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
        print("Name\tArrival Time\tBurst Time")
        for t in self.tasks:
            print(f"{t['name']}\t{t['arrival']}\t\t{t['burst']}")

    def add_task(self, name, arrival, burst):
        self.tasks.append({"name": name, "arrival": arrival, "burst": burst, "remaining": burst})
        print("Task added.")

    def fcfs_schedule(self):
        if not self.tasks:
            print("No tasks to schedule.")
            return
        # Sort tasks by arrival time
        sorted_tasks = sorted(self.tasks, key=lambda x: x['arrival'])
        current_time = 0
        schedule = []
        waiting_times = {}
        for task in sorted_tasks:
            if current_time < task['arrival']:
                current_time = task['arrival']
            start_time = current_time
            current_time += task['burst']
            end_time = current_time
            schedule.append((task['name'], start_time, end_time))
            waiting_times[task['name']] = start_time - task['arrival']
        
        print("\nFCFS Schedule:")
        print("Task\tStart\tEnd")
        for name, start, end in schedule:
            print(f"{name}\t{start}\t{end}")
        
        avg_waiting = sum(waiting_times.values()) / len(waiting_times)
        print(f"\nAverage Waiting Time: {avg_waiting:.2f}")


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
                burst = int(input("Enter burst time: "))
                if burst <= 0:
                    print("Burst time must be positive.")
                    continue
                scheduler.add_task(name, arrival, burst)
            except ValueError:
                print("Please enter valid numbers for times.")
        elif choice == '3':
            scheduler.fcfs_schedule()
        elif choice == '4':
            print("Exiting the Task Scheduler. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()