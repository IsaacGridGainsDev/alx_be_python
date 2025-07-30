num1 = int(input("Enter any integer: "))
num2 = int(input("Enter another integer: "))

try:
	result = num1 / num2
except ZeroDivisionError:
	print("Your computer cannot handle a division by zero, get a quantum computer!")
else:
	print(f"The division betweeon {num1} and {num2} is {result}")

