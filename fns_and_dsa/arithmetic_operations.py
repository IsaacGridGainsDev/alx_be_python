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
			if num2 == 0:
				print("cannot divide by zero")
			elif num1 == 0 and num2 == 0:
				print("you are beaking the program")
			else:
				answer = num1 / num2
				return answer
		else:
			print("invalid operation")
			return float("nan")
