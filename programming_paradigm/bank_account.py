import os#for memory

class BankAccount:
	"""A simple object that simulates a financial application"""
	def __init__(self, account_balance=0):
		self.file_path = 'balance.txt'
		self.account_balance = self.load_balance() if os.path.exists(self.file_path) else account_balance
	
	def deposit(self, amount):
		self.account_balance += amount
		self.save_balance()
		return self.account_balance

	def withdraw(self, amount):
		if self.account_balance < amount or self.account_balance == 0:
			return False
		else:
			self.account_balance -= amount
			self.save_balance()
			return True
	def display_balance(self):
		print(f"Current Balance: ${self.account_balance}")
	
	def save_balance(self):
		with open(self.file_path, 'w') as f:
			f.write(str(self.account_balance))
	def load_balance(self):
		with open(self.file_path, 'r') as f:
			return float(f.read())

