def greet(name="World"):
	names = input("Enter your first name: ")
	match names:
		case "":
			print(f"Hello {name}!")
		case _:
			print(f"Hello {names}!")
greet()
