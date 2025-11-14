task_desc = input("Enter your task: ")
priority = input("Priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task_desc}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task_desc}' is a high priority task but not urgent!")
    case "low":
        if time_bound == "no":
         print(f"Note: '{task_desc}' is a low priority task. Consider completing it when you have free time.")
        