#learning classes

class Student:
	def __init__(self, name: 'str', age: 'int', class_name: 'str'):
		self.name = name
		self.age = age
		self.class_name = class_name
		self.grade = {'math':0, 'eng':0, 'bio':0, 'chem':0, 'phy':0}
		self.gpa = 0.0

	def grades(self, grade):
		self.grade = grade
		return grade

	def performance(self):
		total = sum(self.grade.values())
		self.gpa = float(total / len(self.grade))
		print(f"{self.name}'s grade is {self.gpa}")
		return self.gpa

	def display_information(self):
		if self.gpa == 0.0:
			print("Grades have not been calculated yet")
			self.performance()
		print(
			f"""
				Name: {self.name}
				Age: {self.age}
				Class: {self.class_name}
				GPA: {self.gpa}
				Grades: """ + "\n".join([f" {subject}: {score}" for subject, score in self.grade.items()])			
		)
student1 = Student("Michael", 18, "Grade 12")
student1.display_information()
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
student2.display_information()
student2.performance()
		
