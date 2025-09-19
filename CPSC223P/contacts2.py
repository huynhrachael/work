# Rachael Huynh
# CWID: 886351212
# September 4th, 2025
# Create a Employee contact list which contains a list of contacts that can be modified and deleted

first_name = []
last_name = []
contact_list =[]

def print_list():
	"""Print all the contacts that are in the contact list"""
	#print(" *** EMPLOYEE CONTACT MAIN MENU  ")
	print("=============== CONTACT LIST ===============")
	print("Index   First Name            Last Name")
	print("=====   ===========           =========")
	for i in range(len(contact_list)):
		print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}')

def add_contact(contact_list,/, *, first_name, last_name):
	"""Add new contact to the contact list"""
	first_name = input("Enter First Name: ")
	last_name = input("Enter Last Name: ")
	newContact = [first_name, last_name]
	contact_list.append(newContact)
	#print(contact_list)
	
def modify_contact(contact_list,/, *,first_name, last_name, modify_index):
	"""Modify the contact list"""
	modify_index = int(input("Which contact index would you like to modify? "))	
	first_name = input("Enter First Name: ")
	last_name = input("Enter Last Name: ")
	if modify_index in range(len(contact_list)):
		contact_list[modify_index][0] = first_name
		contact_list[modify_index][1] = last_name
		return True
	elif modify_index not in range(len(contact_list)):
		print("Invalid index number")
		return False
		

def delete_contact(contact_list,/,*,delete_index):
	"""Delete a contact from the contact list"""
	delete_index = int(input("Which contact index would you like to delete? "))
	if delete_index in range(len(contact_list)):
		del contact_list[delete_index]
		return True
	else :
		print("Invalid index number")
		return False
		
def sort_contacts(contact_list,/,*,column):
	#name = contact_list 
	#for name in range(len(contact_list)):
	#	if contact_list[name][0]:
	#		return first_name
	#	elif contact_list[name][1]:
	#		return last_name
	if column == 0:
		contact_list.sort(key = lambda x:x[0].lower())
	elif column == 1:
		contact_list.sort(key = lambda x:x[1].lower())	
	else:
		print("Invalid")
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
