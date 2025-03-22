from supabase import create_client

# Replace with your Supabase URL and Anon Key
SUPABASE_URL = "https://mawhlnsiuhpzgiqmhpfx.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1hd2hsbnNpdWhwemdpcW1ocGZ4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDI2NDE4OTcsImV4cCI6MjA1ODIxNzg5N30.yalO9PjS3EhlgMqpmdVmlZgMbaNwqEYp4oJL9xxVJmE"

# Create a Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


def add_task(task):
    result = supabase.table("tasks").insert({"task": task}).execute()
    print("Task added:", result)


def list_tasks():
    result = supabase.table("tasks").select("*").execute()
    if result.data:  # Accessing the `.data` property
        print("Your Tasks:")
        for task in result.data:
            status = "✅" if task['completed'] else "❌"
            print(f"{task['id']}: {task['task']} {status}")
    else:
        print("No tasks found.")


def mark_task_completed(task_id):
    result = supabase.table("tasks").update({"completed": True}).eq("id", task_id).execute()
    print("Task marked as completed:", result)


def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Mark a task as completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Enter the task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Ensure the script runs the menu only when executed directly
if __name__ == "__main__":
    main()
