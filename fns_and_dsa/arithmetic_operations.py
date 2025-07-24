def perform_operation(num1, num2, operation):
	match operation:
		case '+' | 'add':
			answer = num1 + num2
			return answer
		case '-' | 'subtract':
			if num1 > num2:
				answer = num1 - num2
				return answer
			else:
				answer = num2 - num1
				return answer
		case '*' | 'multiply':
			answer = num1 * num2
			return answer
		case '/' | 'divide':
			try:
				answer = num1 / num2
			except ZeroDivisionError:
				print("cannot divide by zero! ")
				return float("inf")
			else:
				return answer
		case _:
			print("invalid operation")
			return float("nan")
