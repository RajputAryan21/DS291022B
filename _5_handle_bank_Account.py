class Account:
	def __init__(self, title=None, balance=0):
		self.title = title
		self.balance = balance

	def withdrawal(self, amount):
		self.balance -= amount

	def deposit(self, amount):
		self.balance += amount

	def getBalance(self):
		return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.interestRate*self.getBalance())/100

#code to test - do not edit this

demo1 = SavingsAccount("Ashish", 2000, 5)

print("Balance at start:", demo1.getBalance())
print("Interest Amount at start:", demo1.interestAmount())
demo1.deposit(500)
print("\nBalance after deposit of 500:", demo1.getBalance())
print("Interest Amount after deposit:", demo1.interestAmount())
demo1.withdrawal(1000)
print("\nBalance after withdrawal of 1000:", demo1.getBalance())
print("Interest Amount after withdrawl:", demo1.interestAmount())