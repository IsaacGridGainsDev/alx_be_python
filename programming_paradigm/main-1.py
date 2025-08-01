from library_management import Book, Library

def main():
	#setup a small library
	library = Library()
	library.add_book(Book("Brave New World", "Aldous Huxley"))
	library.add_book(Book("1984", "George Orwell"))

	#Initial list of availble books
	print("Available books after setup:")
	library.list_available_books()
	
	#simulate checking out a book
	library.check_out_book("1984")
	print("\nAvailable after checking out '1984':")
	library.list_available_books()

	#simulate returning a book
	library.return_book("1984")
	print("\nAvailable books after returning '1984':")
	library.list_available_books()

if __name__ == "__main__":
	main()
