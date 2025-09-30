import hashlib
import os

alphabets = 'abcdefghijklmnopqrstuvwxyz'

def encrypt_file(input_file, output_file, key):
	try:
		with open(input_file, 'r') as file:
			lines = file.readlines()
		print(lines)		
		with open(output_file, 'a') as file:
			for line in lines:
				file.write(encrypt(line, key))
		print(line)
	except FileNotFoundError:
		print(f"Error: {input_file} not found!")
	

def decrypt_file(input_file, output_file, key):
	try:
		with open(input_file, 'r') as file:
			lines = file.readlines()
			print(lines)
			
		with open(output_file, 'w') as file:
			for line in lines:
				file.write(decrypt(line,key))
	except FileNotFoundError:
		print(f"Error: {intput_file} not found!")
def encrypt(line, key):
	encrypted_text = ' '
	for k in line.lower():
		try:
			i = (alphabets.index(k) + key) % 26
			encrypted_text += alphabets[i]
		except ValueError:
			encrypted_text += k
		return encrypted_text.lower()
	print(encrypted_text) 


def decrypt(text,key):
	decrypted_text = ' '
	for k in text.lower():
		try:
			i = (alphabets.index(k) - key) % 26
			decrypted_text += alphabets[i]	
		except ValueError:
			decrypted_text += k
		return decrypted_text.lower()
		
if __name__ == "__main__":
	print("1. Encrypt a file: ")
	print("2. Decrypt a file: ")
	
	choice = int(input("Enter your choice: "))
	input_file = input("Enter the input file name: ")
	output_file = input("Enter the output file name: ")
	key = int(input("Enter the encryption/decryption key (integer): "))
	
	if choice == 1:
		encrypt_file(input_file, output_file, key)
	elif choice == 2:
		decrypt_file(input_file, output_file, key)
		
	else:
		print("Invalid choice. ")
	
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
				
