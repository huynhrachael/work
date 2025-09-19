# Rachael Huynh
# CWID: 886351212
# September 18th, 2025
# Create a Employee contact list which contains a list of contacts that can be modified and deleted

#first_name = []
#last_name = []

contact_dict = {}

def add_contact(contact_dict,/, *, id, first_name, last_name):
	"""Add new contact to the contact dictionary"""
	id = input("Enter phone number: ")
	first_name = input("Enter First Name: ")
	last_name = input("Enter Last Name: ")
	newContact = [first_name, last_name]
	contact_dict[id]= newContact
	if id in range(len(contact_dict)):
		print("Phone number already exists")
		return "error"
	elif id not in range(len(contact_dict)):
		contact_dict[id].append(newContact)
		return newContact
	#contact_dict = {input("Enter phone number: "): input("Enter First Name: ") input("Enter Last Name: ")	
	
	
def modify_contact(contact_dict,/, *, id, first_name, last_name):
	"""Modify the contact list"""
	id = input("Enter phone number: ")
	first_name = input("Enter First Name: ")
	last_name = input("Enter Last Name: ")
	if id in range(len(contact_dict)):
		contact_dict[id][0] = first_name
		contact_dict[id][1] = last_name
		print("Modified: ")
		return contact_dict
	elif id not in range(len(contact_dict)):
		print("Phone number does not exist. ")
		return "error"

def delete_contact(contact_dict,/,*, id):
	id = input("Enter phone number: ")
	if id not in range(len(contact_dict)):
		print("Invalid phone number.")
	elif id in range(len(contact_dict)):
		del contact_dict[id][0]
		del contact_dict[id][1]
		return contact_dict

def sort_contacts(contact_dict,/):
	contact_dict = {key: contact_dict[key] for key in sorted(contact_dict)}
	return contact_dict
	
def find_contact(contact_dict,/,*, find):
	newContact_dict = {}
	find = contact_dict[id]
	if find in range(len(contact_dict[id][first_name])):
		newContact_dict.append(contact_dict[id])
		Newcontact_dict = {key: Newcontact_dict[key] for key in sorted(Newcontact_dict)}
		return newContact_dict
	elif find in range(len(contact_dict[id][last_name])):
		newContact_dict.append(contact_dict[id])
		Newcontact_dict = {key: Newcontact_dict[key] for key in sorted(Newcontact_dict)}
		return newContact_dict
		 
	
	
	
	
	
	

