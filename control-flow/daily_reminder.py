# Prompt the user for input
task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

# Create customized reminder using match-case
match priority:
    case "high":
        reminder = print(f"Reminder: '{task}' is a high priority task")
    case "medium":
        reminder = print(f"Reminder: '{task}' is a medium priority task")
    case "low":
        reminder = print(f"Note: '{task}' is a low priority task")
    case _:
        reminder = print(f"Note: '{task}' has an unknown priority level")

# Add time sensitivity info
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority == "low":
    reminder += ". Consider completing it when you have free time."

# Display the final message
print(reminder)