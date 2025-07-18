task = input("Enter task description details: ")
priority = input("Enter task priority, (high/medium/low): ")
time_bound = input("Is the task time-bound, yes/no: ")

match priority:
	case "high":
		if time_bound == "yes":
			print(f"'{task}' is a high priority task that requires immediate attention today!")
		else:
			print(f"'{task}' is a high priority task. Consider completing it when you have free time.")
	case "medium":
		if time_bound == "yes":
                        print(f"'{task}' is a medium priority task that requires your immediate attention today!")
		else:
			print(f"'{task} is a medium priority task. Consider completing it when you have free time.") 
	case "low":
		if time_bound == "yes":
                        print(f"'{task}' is a low priority task but is time-bound. Complete it today!")
		else:
			print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
	case _:
		print("you have entered undefined parameters")
