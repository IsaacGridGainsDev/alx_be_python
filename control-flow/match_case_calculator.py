num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

match operation:
	case "+":
		print(num1+num2)
	case "-":
		print(num1-num2)
	case "*":
		print(num1*num2)
	case "/":
		if ZeroDivisionError:
			print("You cannot divide by zero")
		else:
			print(num1/num2)
	case _:
		print("wrong input")
	
