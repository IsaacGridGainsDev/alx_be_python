class Animal:
	def __init__(self):
		pass
	def make_sound(self):
		print("Generic sound")

class Dog(Animal):
	def make_sound(self):
		print("woof!")
class Cat(Animal):
	def make_sound(self):
		print("meoww")
class Bird(Animal):
	def make_sound(self):
		print("chirp!!")

animals = [Animal(), Dog(), Cat(), Bird()]

def let_them_speak(obj):
	for animal in obj:
		animal.make_sound()

let_them_speak(animals)
