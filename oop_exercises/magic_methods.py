class Book:
	def __init__(self, title: str, author: str, pages: int):
		self.title = title
		self.author = author
		self.pages = pages
	def __str__(self):
		return f"Book({self.pages} pages): {self.title} by {self.author}"
	def __repr__(self):
		return f"{self.title} is written by {self.author}, in {self.pages} page(s)"
ada = Book("ada love", "Ada", 40)
print(ada)
