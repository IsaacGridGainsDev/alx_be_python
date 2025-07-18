#Defining a list of predefined weather conditions
user_input = input("What's the weather like today? (sunny/rainy/cold)").lower()

#creating a match-case control flow gate
match user_input:
	case "sunny":
		print("Wear a t-shirt and sunglasses.")
	case "rainy":
		print("Don't forget your umbrella and a raincoat.")
	case "cold":
		print("Make sure to wear a warm coat and a scarf.")
	case _:
		print("Sorry, I don't have recommendations for this weather.")
