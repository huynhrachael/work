# Rachael Huynh
# CWID: 886351212
# September 4th, 2025
# Create a Employee contact list which contains a list of contacts that can be modified and deleted

from contacts2 import*

while True:
	print(" *** EMPLOYEE CONTACT MAIN MENU  ")
	print("1. Print List")
	print("2. Add Contact")
	print("3. Modify Contact")
	print("4. Delete Contact")
	print("5. Sort list by first name: ")
	print("6. Sort list by last name: ")
	print("7. Exit the program")
		
	menu_choice = input("Enter a menu choice(number): ")
		
	if menu_choice == "1":
		print_list()
	elif menu_choice == "2":
		add_contact(contact_list, first_name = "rachael", last_name = "huynh")
	elif menu_choice == "3":
		modify_contact(contact_list, first_name= "rachael", last_name = "huynh", modify_index = 1)
	elif menu_choice == "4":
		delete_contact(contact_list, delete_index = 0)
	elif menu_choice == "5":
		#sort_contacts(contact_list[name][0])
		sort_contacts(contact_list, column = 0)
	elif menu_choice == "6":
		#sort_contacts(contact_list[name][1])
		#print(sorted(last_name))
		sort_contacts(contact_list, column = 1) 
	elif menu_choice == "7":
		print("Exit the program ")
		break
		
		
		
		
		
		
		
		
		
		
		

