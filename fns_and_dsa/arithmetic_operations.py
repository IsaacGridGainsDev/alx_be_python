def perform_operation(num1, num2, operation):
		if operation == '+' or operation == 'add':
			answer = num1 + num2
			return answer
		if operation == '-' or operation == 'subtract':
			if num1 > num2:
				answer = num1 - num2
				return answer
			else:
				answer = num2 - num1
				return answer
		if operation == '*' or operation == 'multiply':
			answer = num1 * num2
			return answer
		if operation == '/' or operation == 'divide':
			try:
				answer = num1 / num2
			except ZeroDivisionError:
				print("cannot divide by zero! ")
				return float("inf")
			else:
				return answer
		else:
			print("invalid operation")
			return float("nan")
