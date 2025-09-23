# Rachael Huynh
# CWID: 886351212
# September 18th, 2025
# Create a Employee contact list which contains a list of contacts that can be modified and deleted

#first_name = []
#last_name = []

contact_dict = {}

def print_dict():
	print("=============== CONTACT LIST ===============")
	print("Last Name    First Name            Phone")
	print("==========   ===========           =========")
	for k, v in contact_dict.items():
		print("{} : {}".format(k, v))
		 
def add_contact(contact_dict,/, *, id, first_name, last_name):
	"""Add new contact to the contact dictionary"""
	id = input("Enter phone number: ")
	first_name = input("Enter First Name: ")
	last_name = input("Enter Last Name: ")
	new_contact = [first_name, last_name]
	contact_dict= {id : new_contact}
	if id is not int:
		return False	
		print("invalid input. Non-numeric value.")
	if id in range(len(contact_dict)):
		print("Phone number already exists")
		return "error"
	elif id not in range(len(contact_dict)):
		contact_dict[id] = new_contact
		return contact_dict	
	
	
def modify_contact(contact_dict,/, *, id, first_name, last_name):
	"""Modify the contact list"""
	id = input("Enter phone number: ")
	first_name = input("Enter First Name: ")
	last_name = input("Enter Last Name: ")
	
	if id in range(len(contact_dict)):
		print("Modified: ", contact_dict[id])
		return contact_dict
	elif id not in range(len(contact_dict)):
		print("Phone number does not exist. ")
		return "error"

def delete_contact(contact_dict,/,*, id):
	id = input("Enter phone number: ")
	if id.isdigit():
		return true
	else:
		print("Invalid input. Non-numeric value.")
	if id not in range(len(contact_dict)):
		print("Invalid phone number.")
	elif id in range(len(contact_dict)):
		del contact_dict[id]
		return contact_dict	

def sort_contacts(contact_dict,/):
	contact_dict = {key: contact_dict[key] for key in sorted(contact_dict)}
	return contact_dict
	
def find_contact(contact_dict,/,*, find):
	find = contact_dict[id]
	if find in range(len(contact_dict[id][first_name])):
		newContact_dict.append(contact_dict[id])
		Newcontact_dict = {key: Newcontact_dict[key] for key in sorted(Newcontact_dict)}
		return newContact_dict
	elif find in range(len(contact_dict[id][last_name])):
		newContact_dict.append(contact_dict[id])
		Newcontact_dict = {key: Newcontact_dict[key] for key in sorted(Newcontact_dict)}
		return newContact_dict
		

		 
	
	
	
	
	
	

