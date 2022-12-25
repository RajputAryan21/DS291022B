from App_user import User
import pwinput

# Please download 'pwinput' module on your system in order for it to work

class UserOperations:
	user_data = []
	order_history = []

	def Register(self):
		while True:
			try:
				print("\n----------------Register Account------------------\n")
				name = input("Enter Full Name: ")
				phone_num = int(input("Enter phone number: "))
				email = input("Enter Email: ")
				address = input("Enter Address: ")
				password = pwinput.pwinput("Enter Password: ")                     # pwinput will show user input as '*' to not show the password on screen
				user = User(name=name,phone_num=phone_num,email=email,address=address,password=password)
				self.user_data.append(user)
				print("\nRegistration Complete!")
				break
			except Exception as ex:
						print("Exception occured:", ex)

	def Login(self):
		try:
			print("\n--------------------User Login---------------------\n")
			self.phone_num = int(input("Enter Phone Number: "))
			self.password = pwinput.pwinput("Enter password: ")
			for user in self.user_data:
				if self.phone_num == user.get_phone_num() and self.password == user.get_password():
					return "\nLogin Successful!"
				else:
					return "Login Unsuccessful! Incorrect phone number or password."
		except Exception as ex:
				return f"Exception occured: {ex}"

	def Update_profile(self):
		while True:
			try:
				password = input("\nEnter password to proceed and edit your profile: ")
				for user in self.user_data:
					if password == user.get_password():
						print("\nCorrect Password.\n")
						user.set_name(input("Enter Full Name: "))
						user.set_phone_num(int(input("Enter phone number: ")))
						user.set_email(input("Enter Email: "))
						user.set_address(input("Enter Address: "))
						return "\nProfile Updated Successfully!\n"
					else:
						print("Incorrect Password!\n")
			except Exception as ex:
				print("Exception occured:", ex)
		
	def View_profile(self):
		for user in self.user_data:
			print("\n--------------User Profile---------------\n")
			print(user)

	def Place_order(self):
		menu = {1 : "Tandoori Chicken (4 pieces) [INR 240]",
				2 : "Vegan Burger (1 Piece) [INR 320]",
				3 : "Truffle Cake (500gm) [INR 900]"
				}

		option = []
		print("\n-----------------Place Order----------------\n")
		print("1. Tandoori Chicken (4 pieces) [INR 240] \n2. Vegan Burger (1 Piece) [INR 320] \n3. Truffle Cake (500gm) [INR 900] \n4. Proceed with order \nNote: Please enter one option no at a time.")
		
		# This while loop takes input for items the user want to add to their order and stores it in a list, if the user enters an option which 
		# is not in the menu, a message appears letting the user know that the option enetered is invalid

		while True:
			num = int(input(f"\nEnter the appropriate option no: "))
			if num in [1,2,3]:
				print("Item added!")
				option.append(num)
			elif num == 4:
				break
			else:
				print("Invalid option entered!\n")
				
		count_1 = 0
		count_2 = 0
		count_3 = 0
		for i in range(len(option)):
			if option[i] == 1:
				count_1 += 1
			elif option[i] == 2:
				count_2 += 1
			else:
				count_3 += 1

		self.order_lst = []

		print("\n------------Selected Items------------\n")
		if 1 in option:
			data_1 = f"{menu[1]} X {count_1}"
			self.order_lst.append(data_1)
			print(data_1,"\n")
		if 2 in option:
			data_2 = f"{menu[2]} X {count_2}"
			self.order_lst.append(data_2)
			print(data_2,"\n")
		if 3 in option:
			data_3 = f"{menu[3]} X {count_3}"
			self.order_lst.append(data_3)
			print(data_3)
		
		while True:
			print("\n1. Confirm order \n2. Cancel order\n")
			ans = int(input("Enter the appropriate option no: "))

			if ans == 1:
				print("\nOrder confirmed!\n")
				self.Order_history(self.order_lst)
				break
			elif ans ==2 :
				print("\nOrder cancelled successfully!\n")
				if count_1>0:
					self.order_lst.remove(data_1)
				if count_2>0:
					self.order_lst.remove(data_2)
				if count_3>0:
					self.order_lst.remove(data_3)		
				break
			else:
				print("Invalid option!\n")

	def Order_history(self,lst):
		self.order_history.append(lst)
		
	def Print_order_history(self):
		if len(self.order_history) >= 1:
			for i in range(len(self.order_history)):
				print(f"\n---- Order no. {i+1} ----\n")
				for j in self.order_history[i]:
					print(j)
		else:
			print("\nEmpty Order History!\n")