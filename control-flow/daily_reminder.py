# Prompt the user for input
task = input("Enter your priority task for today: ")
priority = input("Set the task's priority (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Match case block to handle priority levels
match priority:
    case "high":
        reminder = f"🔴 High-priority task: {task}."
    case "medium":
        reminder = f"🟠 Medium-priority task: {task}."
    case "low":
        reminder = f"🟢 Low-priority task: {task}."
    case _:
        reminder = f"⚪ Unknown-priority task: {task}."

# Add time sensitivity info
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Display the reminder multiple times using a loop
for i in range(1, 2):  # just once for now, but expandable
    print(reminder)
