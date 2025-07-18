rows = int(input("Enter the size of the pattern: "))
row_count = 0
while row_count < rows:
	row_count += 1
	for row in range(0, rows):
		print("*", end="")
	print()
