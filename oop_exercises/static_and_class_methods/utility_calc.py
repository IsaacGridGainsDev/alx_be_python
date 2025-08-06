class Calculator:
	def __init__(self):
		pass
	@staticmethod
	def add(x,y):
		return x+y
	def multiply(x,y):
		return x*y

print(Calculator.add(10,3))
print(Calculator.multiply(-2,-19))
