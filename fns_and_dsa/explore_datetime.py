from datetime import datetime, timedelta, date

def display_current_datetime():
	current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S%p")
	print(f"Current data and time: {current_date}")
display_current_datetime()

def calculate_future_date():
	number_of_days = int(input("Enter the number of days to add to the current date: "))
	current_date = datetime.now()
	future_date = (current_date + timedelta(days=number_of_days)).strftime("%Y-%m-%d")
	print(f"Future date: {future_date}")
calculate_future_date()
