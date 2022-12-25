from App_user_operations import UserOperations
from App_admin_operations import AdminOperations

class Main:
	def user_execute(self,choice,user_operations):
		if choice == 1:
			user_operations.Place_order()
		elif choice == 2:
			user_operations.Print_order_history()
		elif choice == 3:
			data = user_operations.Update_profile()
			print(data)
		elif choice == 4:
			user_operations.View_profile()

	def admin_execute(self,choice,admin_operations):
		if choice == 1:
			admin_operations.add_item()
		elif choice == 2:
			admin_operations.edit_item()
		elif choice == 3:
			admin_operations.view_item()
		elif choice == 4:
			admin_operations.remove_item()


if __name__ == "__main__":
	obj = Main()
	user_operations = UserOperations()
	admin_operations = AdminOperations()


	while True:
		try:
			print("------------------Welcome-------------------")
			login = int(input("\n1. User Login \n2. Admin Login \n3. Exit \n\nEnter the appropriate option no: "))
			if login == 1:
				try:
					user_operations.Register()
					while True:
						login = user_operations.Login()
						print(login)
						if login == "\nLogin Successful!" :
							break
					while True:
						print("------------------Main Menu-------------------")
						choice = int(input("\n1. Place New Order \n2. Order History \n3. Update Profile \n4. View Profile \n5. Exit to start menu \n\nEnter the appropriate option no: "))	
						if choice == 5:
							break
						obj.user_execute(choice=choice,user_operations=user_operations)
				except Exception as ex:
					print("Exception occured:", ex)
			elif login == 2:
				try:
					data = admin_operations.Login()
					print(data)
					if data :
						while True:
							try:
								print("------------------Main Menu-------------------")
								choice = int(input("\n1. Add Food Items \n2. Edit Items \n3. View Items \n4. Remove Food Item \n5. Exit to main menu \nEnter the appropriate option no: "))	
								if choice == 5:
									break
								obj.admin_execute(choice=choice,admin_operations=admin_operations)
							except Exception as ex:
								print("\nException occured:", ex)
				except Exception as ex:
					print("Exception occured:", ex)
			elif login == 3:
					break
			else:
					print("\nInvalid Option!")
		except Exception as ex:
				print("\nException occured:", ex)