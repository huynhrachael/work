# Rachael Huynh
# CWID: 886351212
# September 30th, 2025
# Create a Employee contact list which contains a list of contacts that can be modified and deleted

from contacts3 import*
contact_dict = {}
while True:
	print(" *** EMPLOYEE CONTACT MAIN MENU  ")
	print("1. Add Contact")
	print("2. Modify Contact")
	print("3. Delete Contact")
	print("4. Print Contact List")
	print("5. Find Contact ")
	print("6. Exit the program ")
		
	menu_choice = input("Enter a menu choice(number): ")
		
	if menu_choice == "1":
		add_contact(contact_dict, id = '0', first_name = 'rachael', last_name = 'huynh')
	elif menu_choice == "2":
		modify_contact(contact_dict,id = "0", first_name= "rachael", last_name = "huynh",)
	elif menu_choice == "3":
		delete_contact(contact_dict, id = "0")
	elif menu_choice == "4":
		print_dict(contact_dict)
	elif menu_choice == "5":
		find_contact(contact_dict, find = 'huynh')
	elif menu_choice == "6":
		print("Exit the program")
		break
		
