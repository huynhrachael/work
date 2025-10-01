# Rachael Huynh
# CWID: 886351212
# September 30th, 2025
# Create a Employee contact list which contains a list of contacts that can be modified and deleted

#first_name = []
#last_name = []

contact_dict = {}

def print_dict(contact_dict):
	print("=============== CONTACT LIST ===============")
	print("Last Name    First Name            Phone")
	print("==========   ===========           =========")
	for k, v in contact_dict.items():
		print(f'{v[1]:13}{v[0]:21}{k:10}')
		 
def add_contact(contact_dict,/, *, id, first_name, last_name):
	"""Add new contact to the contact dictionary"""
	while True:
		try:
			id = int(input("Enter phone number: "))
			first_name = input("Enter First Name: ")
			last_name = input("Enter Last Name: ")
			new_contact = [first_name, last_name]
			if id in contact_dict:	
				print("PHONE NUMBERS ALREADY EXISTS.")
				return "error"
			print("Added: ", new_contact)	
			contact_dict[id]= new_contact
			return contact_dict
		except ValueError:
			print("INVALID PHONE NUMBER. ")
		
	
def modify_contact(contact_dict,/, *, id, first_name, last_name):
	"""Modify the contact list"""
	while True:
		try:
			id = int(input("Enter phone number: "))
			first_name = input("Enter First Name: ")
			last_name = input("Enter Last Name: ")
			modify_contact = [first_name, last_name]
			if id not in contact_dict:	
				print("PHONE NUMBERS DOESN'T EXIST.")
				return "error"
			contact_dict[id] = modify_contact
			print("Modified: ", modify_contact )
			return contact_dict
		except ValueError:
			print("INVALID MODIFICATION. ")
	
	
def delete_contact(contact_dict,/,*, id):
	while True:
		try:
			id = int(input("Enter phone number: "))
			if id not in contact_dict:
				print("PHONE NUMBER DOESN'T EXIST.")
			elif id in contact_dict:
				r = contact_dict.pop(id)
				print("Delete: ", r)
			return contact_dict
		except ValueError:
			print("INVALID DELETE.")	
			
def sort_contacts(contact_dict,/):
	sort_contact_dict = sorted(contact_dict.items(), key = lambda v: v[1][1].lower())
	return sort_contact_dict
	
def find_contact(contact_dict,/,*, find):
	find_contact = {}
	find = input("Enter Search String: ")
	for k,v in contact_dict.items():
		if find in v[1].lower():
			find_contact[k] = v
			sort_contact = dict(sorted(find_contact.items(), key = lambda v: v[1][1].lower()))
		'''if find in v:
			find_contact[k] = v
			sort_contact = dict(sorted(find_contact.items(), key = lambda k: string(k[1][1]).lower()))
		'''

	print("=============== FOUND CONTACT(S) ===============")
	print("Last Name    First Name         Phone")
	print("==========   ===========        =========")
	for k, v in sort_contact.items():
		print(f'{v[1]:13}{v[0]:21}{k:10}')
		
	return sort_contact
		
	

		 
	
	
	
	
	
	

