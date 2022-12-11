class Calculator:

	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def add(self):
		return self.num1 + self.num2

	def subtract(self):
		return self.num2 - self.num1 

	def multiply(self):
		return self.num1 * self.num2

	def divide(self):
		return self.num2 / self.num1

num1,num2 = input("Enter two numbers: ").split()

calculator = Calculator(int(num1), int(num2))
print(f"Result after addition: {calculator.add()}")
print(f"Result after subtraction: {calculator.subtract()}")
print(f"Result after multiplication: {calculator.multiply()}")
print(f"Result after division: {calculator.divide()}")