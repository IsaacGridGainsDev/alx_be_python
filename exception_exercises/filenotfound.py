try:
	with open("file.txt", "r") as file:
		print(file.read())
except FileNotFoundError:
	print("file no where")
