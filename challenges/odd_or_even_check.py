def odd_or_even(number=None):
	while number in (None, ""):
		user = int(input("Enter any positive integer: "))
		number = user

	if number % 2 == 0:
		print(f"{number} is an even number")
	else:
		print(f"{number} is an odd number")
odd_or_even()
