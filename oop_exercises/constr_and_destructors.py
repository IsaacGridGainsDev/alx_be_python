class Person:
	def __init__(self, name: str, age: int):
		self.name = name
		self.age = age
	def __del__(self):
		return f"Goodbye! {self.name}"

man = Person("Isaac", 24)
man
