# Rachael Huynh
# CWID: 886351212
# September 4th, 2025
# Create a Employee contact list which contains a list of contacts that can be modified and deleted

from contacts import*


#def main(contact_list):

#print(" *** EMPLOYEE CONTACT MAIN MENU  ")
while True:
	print(" *** EMPLOYEE CONTACT MAIN MENU  ")
	print("1. Print List")
	print("2. Add Contact")
	print("3. Modify Contact")
	print("4. Delete Contact")
	print("5. Exit the program")
		
	menu_choice = input("Enter a menu choice(number): ")
		
	if menu_choice == "1":
		#print(contact_list)
		print_list()
	elif menu_choice == "2":
		add_contact(contact_list)
	elif menu_choice == "3":
		modify_contact(contact_list)
	elif menu_choice == "4":
		delete_contact(contact_list)
	elif menu_choice == "5":
		print("Exit the program ")
		break
			
			
			
			
			
			
			
			
			
			
			
			
			
			
