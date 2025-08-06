class Person:
	child_count = 0
	
	def __init__(self, name: str, age: int):
		self.name = name
		self.age = age

	@classmethod
	def create_child(cls):
		cls.age = 0
		cls.child_count += 1
		print(f"total children: {cls.child_count}")

person1 = Person("ade", 10).create_child()
person2 = Person("femi", 10).create_child()
