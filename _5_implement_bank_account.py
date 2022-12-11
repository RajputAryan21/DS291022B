class Account:
	
	def __init__(self, title=None, balance=0):
		self.title = title
		self.balance = balance

class SavingsAccount(Account):

	def __init__(self, title=None, balance=0, interestRate=0):
		super().__init__(title, balance)
		self.interestRate = interestRate
		

title = input("Enter Title: ")
balance = input("Enter Balance: ")
interest = input("Enter Interest rate: ")

obj = SavingsAccount(title,balance,interest)

print(f"Title: {obj.title} \nBalance: {obj.balance} \nInterest rate: {obj.interestRate}")