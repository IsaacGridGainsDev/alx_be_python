FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
	temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
	return temp
def convert_to_fahrenheit(celsius):
	temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
	return temp

def main():
	try:
		user_temp = float(input("Enter the temperature to convert: "))
	except ValueError:
		print("Invalid temperature. Please enter a numeric value.")
	temp_format = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
	match temp_format:
		case 'C' | 'c':
			converted_temp = convert_to_fahrenheit(user_temp)
			print(f"{user_temp:.1f}C is {converted_temp:.4f}F")
		case 'F'| 'f':
			converted_temp = convert_to_celsius(user_temp)
			print(f"{user_temp:.1f}F is {converted_temp:.4f}C")
		case _:
			print("Invalid temperature. Pleae enter a numeric value.")
main()
