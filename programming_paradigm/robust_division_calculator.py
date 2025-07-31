def safe_divide(numerator, denominator):
	try:
		try:
			result = float(numerator) / float(denominator)
		except ValueError:
			return "Error: Please enter numeric values only."
		else:
			return f"The result of the division is {result:.1f}"
	except ZeroDivisionError:
		return "Error: Cannot divide by zero."
	
