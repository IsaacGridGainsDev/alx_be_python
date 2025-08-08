from book_class import Book

def main():
	#create instance
	my_book = Book("1984", "Goerge Orwell", 1949)

	#Demonstrating the __str__ method
	print(my_book)

	#Demonstrating the __repr__ method
	print(repr(my_book))

	#deleting a book
	del my_book

if __name__ == '__main__':
	main()
