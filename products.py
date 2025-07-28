class Product:
	def __init__(self, name: 'str', price: 'int', quantity: 'int', discount: 'bool'):
		self.name = name
		self.price = price
		self.quantity = quantity
		self.discount = discount

	def product_info(self):
		if self.discount:
			percentage = int(input("Enter percentage of discount: "))
			discounted_price = self.price * (1- (percentage / 100))
			print(
				f"""
					Product Name: {self.name}
					Original Price: {self.price}
					Discounted Price: {discounted_price}
					Quantity in Stock: {self.quantity}
					Discount: {percentage / 100:.2f}			
				"""
			)
		else:
			print(
				f"""
					Product Name: {self.name}
					Price: {self.price}
					Qunatity in Stock: {self.qunatity}
					Discount: None				
				"""
			)
product1= Product("garri", 5000, 40, True)
product1.product_info()
