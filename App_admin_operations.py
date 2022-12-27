from App_admin import Admin
import uuid
import pwinput

# Please download 'pwinput' module on your system in order for it to work
# Refer line 8, for login credentials for Admin
class AdminOperations:
	login_details = {"username" : "admin", "password" : "admin123"}
	item_lst = []
	def Login(self):
		while True:
			try:
				print("\n-------------------Admin Login---------------------\n")
				username = input("Enter username: ")
				password = pwinput.pwinput("Enter password: ")                # pwinput will show user input as '*' to not show the password on screen
				if username == self.login_details["username"] and password == self.login_details["password"]:
					return "Login Successful!"
				else:
					print("Login Unsuccessful! Incorrect username or password.")
			except Exception as ex:
					print("Exception occured:", ex)

	def add_item(self):
		print("\n----------------Add Food Item---------------\n")
		FoodID = str(uuid.uuid4())
		Name = input("Enter Item name: ")
		Quantity = int(input("Enter quantity: "))
		Price = int(input("Enter Item Price: "))
		Discount = int(input("Enter discount available(in percent): "))
		Stock = int(input("Enter amount of Item left in stock: "))
		admin = Admin(FoodID=FoodID,Name=Name,Quantity=Quantity,Price=Price,Discount=Discount,Stock=Stock)
		self.item_lst.append(admin)
		print("\nFood Item added successfully!\n")

	def view_item(self):
		count = 0
		if len(self.item_lst) > 0:
			for i in self.item_lst:
				count += 1
				print(f"\n-----Details of Food Item {count}-----\n \n{i}\n")
		else:
			print("\nNo item. Please add items to view in Item list!")

	def edit_item(self):
		id = input("\nEnter FoodID for the item you want to edit: ")
		item = self.search_by_FoodID(id)
		if item:
			item.set_Name(input("Enter Item name: "))
			item.set_Quantity(input("Enter quantity: "))
			item.set_Price(input("Enter Item Price: "))
			item.set_Discount(input("Enter discount available(in percent): "))
			item.set_Stock(input("Enter amount of Item left in stock: "))
			print("\nItem updated successfully!\n")
		else:
			print("\nItem not found.\n")

	def remove_item(self):
		id = input("\nEnter FoodID for the item you want to remove: ")
		item = self.search_by_FoodID(id)
		if item:
			self.item_lst.remove(item)
			return "\nItem deleted successfully!\n"

	def search_by_FoodID(self,id):
		for item in self.item_lst:
			if item.get_FoodID() == id:
				return item
