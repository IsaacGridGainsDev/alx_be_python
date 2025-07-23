#a simple add, subtract, multiply and divide script
def add(x, y):
	result = x + y
	return result

def subtract(x, y):
	result = x - y
	return result

def multiply(x, y):
	result = x * y
	return result

def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("you cannot divide by zero")
	else:
		return result
