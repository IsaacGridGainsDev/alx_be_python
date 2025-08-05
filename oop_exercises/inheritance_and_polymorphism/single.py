class Shape:
	def __init__(self, length: int, breadth: int):
		self.length = length
		self.breadth = breadth
		self.area = 0
	def calculate_area(self):
		self.area = self.length * self.breadth
		return f"area of shape: {self.area}"
	def __repr__(self):
		return f"shape has length of {self.length}, breadth of {self.breadth}"
class Rectangle(Shape):
	def calculate_area(self):
		self.area = self.length * self.breadth
		print("area: ", self.area)

rect=Rectangle(10,14)
rect.calculate_area()
print(rect)
