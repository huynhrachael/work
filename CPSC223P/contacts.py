# Rachael Huynh
# CWID: 886351212
# September 4th, 2025
# Create a Employee contact list which contains a list of contacts that can be modified and deleted

contact_list =[[first_name,last_name]]

def print_list(contact_list):
	"""Print all the contacts that are in the contact list"""
	for i in range(contact_list):
		#contact_list.append()
		return contact_list
	print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
	
def add_contact(contact_list):
	"""Add new contact to the contact list"""
	for i in range(contact_list):
		first_name = input("Enter First Name: ")
		last_name = input("Enter Last Name: ")
		return (first_name, last_name)
		contact_list.append(i)
	return (contact_list)
	
def modify_contact(contact_list):
	"""Modify the contact list"""
	for i in range(contact_list):
		modify_index = int(input("Which contact index would you like to modify? "))	
		first_name = input("Enter First Name: ")
		last_name = input("Enter Last Name: ")
		contact_list.append(i)
	return (contact_list)
	
def delete_contact(contact_list):
	"""Delete a contact from the contact list"""
	delete_index = int(input("Which contact index would you like to delete? "))
	for i in delete_index:
		contact_list.remove(i)
	return (contact_list)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
