class ValueTooHighError(Exception):
	"""Custom Exception for handling vlaues higher than 100"""
	def __init__(self, value: int):
		self.value = value
	def __str__(self):
		return f"{self.value} is too high"



def check_val(number):
	if number > 100:
		raise ValueTooHighError(number)
	else:
		print("Solid choice!")

number = int(input("Enter any integer: "))
try:
	check_val(number)
except ValueTooHighError as e:
	print(e)
