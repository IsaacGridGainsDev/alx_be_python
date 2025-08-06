class Book:
	count = 0 #To keep track of how many instances are created
	def __init__(self, title: str):
		self.titile = title
		Book.count += 1

	@classmethod
	def display_total_books(cls):
		print(f"Total books created are {cls.count}")

book1 = Book("ABC")
book2 = Book("123")
book3 = Book("Python")
Book.display_total_books()
