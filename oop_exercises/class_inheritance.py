class Animal:
	def __init__(self, name):
		self.name = name
	def eat(self):
		return f"generic answer"
	def sleep(self):
		return f"snore, zzzz!"
	def __repr__(self):
		return f"{self.name} animal species"
class Dog(Animal):
	def __init__(self, name):
		super().__init__(name)
		
	def make_sound(self):
		print("Bark")
	

dog = Dog("buddy")
dog.make_sound()
print(dog)

cat = Animal("mekky")
print(cat)
