# Initialize an empty list to store tasks
tasks = []

def add_task():
  """Gets user input for a new task and adds it to the list"""
  new_task = input("Enter a new task: ")
  tasks.append(new_task)
  print(f"{new_task} added to the list!")

def list_tasks():
  """Prints all tasks in the list"""
  if not tasks:
    print("There are no tasks in the list.")
    return
  print("Your tasks:")
  for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

def remove_task():
  """Removes a task from the list based on user selection"""
  if not tasks:
    print("There are no tasks to remove.")
    return
  list_tasks()
  try:
    task_to_remove = int(input("Enter the number of the task to remove: ")) - 1
    if task_to_remove < 0 or task_to_remove >= len(tasks):
      print("Invalid task number.")
      return
    removed_task = tasks.pop(task_to_remove)
    print(f"{removed_task} removed from the list.")
  except ValueError:
    print("Invalid input. Please enter a number.")

def main():
  """Main loop for the application"""
  while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      add_task()
    elif choice == '2':
      list_tasks()
    elif choice == '3':
      remove_task()
    elif choice == '4':
      print("Exiting the application.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()
