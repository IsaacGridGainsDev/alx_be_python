def display_menu():
	print("Shopping List Manager")
	print("1. Add Item")
	print("2. Remove Item")
	print("3. View List")
	print("4. Exit")

def main():
	shopping_list = []
	while True:
		display_menu()
		choice = input("Enter your choice: ")


		if choice == '1':
		# Prompt for and add an item
			item = input("Enter the item to add: ")
			print(f"{item} has been added into Shopping List")
			shopping_list.append(item)
			pass

		elif choice == '2':
			# Prompt for and remove an item
			item = input("Enter the item to remove: ")
			if item in shopping_list:
				shopping_list.remove(item)
				print(f"{item} has been removed from Shopping List")
			else:
				print(f"{item} not found!")
				pass
		
		elif choice == '3':
			# Display the shopping list
			print(f"Shopping List:{shopping_list}")
			pass

		elif choice == '4':
			print("Goodbye!")
			break

		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()
