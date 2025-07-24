variable = 23

def ipass():
	variable = 24
	print(f"{variable} is local")
ipass()
print(f"{variable} is global")

count = lambda list: (i for i in list)
count([1,2,3,4,5,6,7])

#Ensclosed Namespaces
def count():
	var = 123
	print(var)
def log():
	var=321
	print(var)
count()
log()

