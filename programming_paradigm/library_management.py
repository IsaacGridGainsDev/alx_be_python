class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self._is_checked_out = False
class Library:
	def __init__(self):
		self._books = []
		self._checked_out_books = []

	def add_book(self, book):
		self._books.append(book)

	def check_out_book(self, title):
		for book in self._books:
			if book.title == title:
				book._is_checked_out = True
				self._books.remove(book)
				self._checked_out_books.append(book)
				return self._books
#			print("book not found")		

	def return_book(self, title):
		for book in self._checked_out_books:
			if book.title == title and book._is_checked_out:
				book._is_checked_out = False
				self._books.append(book)
				self._checked_out_books.remove(book)
				return self._books
		
	def list_available_books(self):
		for book in self._books:
			if not book._is_checked_out:
				print(f"{book.title} by {book.author}")
