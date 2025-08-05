class Bird:
	def __init__(self):
		pass
	def fly(self):
		print(" I fly! ")
class Mammal:
	def __init__(self):
		pass
	def run(self):
		print("I walk! ")

class Bat(Bird, Mammal):
	def __init__(self):
		pass

bat = Bat()
bat.run()
bat.fly()
