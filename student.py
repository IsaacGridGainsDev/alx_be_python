#learning classes

class Student:
	def __init__(self, name: 'str', age: 'int', class_name: 'str'):
		self.name = name
		self.age = age
		self.class_name = class_name
		self.grade = {'math':0, 'eng':0, 'bio':0, 'chem':0, 'phy':0}

	def grades(self, grade):
		self.grade = grade
		return grade

	def performance(self):
		total = sum(self.grade.values())
		gpa = float(total / len(self.grade))
		print(f"{self.name}'s grade is {gpa}")

student1 = Student("Michael", 18, "Grade 12")
student1.grades(
	{
		'math': 60,
		'eng': 76,
		'bio': 77,
		'chem': 80,
		'phy': 67

}
)
student1.performance()
						
student2 = Student("Zainab", 24, "SSS 3w")
student2.grades(
	{
		'math': 90,
		'eng': 84,
		'bio': 88,
		'chem': 90,
		'phy': 72

}
)
student2.performance()
		
