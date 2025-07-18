#Defining a list of predefined weather conditions
user_input = input("What's the weather like today? (sunny/rainy/cold):")

#creating a match-case control flow gate
if user_input == "sunny":
	print("Wear a t-shirt and sunglasses.")
elif user_input == "rainy":
	print("Don't forget your umbrella and a raincoat.")
elif "cold":
	print("Make sure to wear a warm coat and a scarf.")
else:
	print("Sorry, I don't have recommendations for this weather.")
