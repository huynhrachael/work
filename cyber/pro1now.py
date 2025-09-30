import string
import random
import hashlib
import os

def encrypt(input_file, output_file, key):
	with open(input_file, 'r') as file:
		text = file.readlines()       #read all lines from open file and return as list of strings
	print(text)
	transposition(text, key)
	encrypt_mess = transposition(text, key)
	#print(ciphertext)
	substitution(text, key, alphabet = 'abcdefghijklmnopqrstuvwxyz')
	#print(map)
 	    		     
	#with open(output_file, 'w') as file:    #open the specified file output_file to write what you want
	#	for line in text:
	#		file.write(transposition(ciphertext))
		
def transposition(text, key):
	num_column = len(key)
	num_rows = (len(text) + num_column -1)
		
	grid = [['' for _ in range(num_column)] for _ in range(num_rows)]
	text_index = 0
	for r in range(num_rows):
		for c in range(num_column):
			if text_index < len(text):
				grid[r][c] = text[text_index]
				text_index +=1
			else:
				grid[r][c]= 'X'
	key_sort_index = sorted(range(num_column), key = lambda k_idx: key[k_idx])
		
	ciphertext =[]
	for column_index in key_sort_index:
		for r in range(num_rows):
			ciphertext.append(grid[r][column_index])
	return "".join(ciphertext)
	with open(output_file, 'w') as file:    #open the specified file output_file to write what you want
		for line in text:
			file.write(transposition[ciphertext])
	

def substitution(text, key, alphabet):
	def generate_key(alphabet):
		shuffle_alphabet = list(alphabet)
		random.shuffle(shuffle_alphabet)
		return "".join(shuffled_alphabet)
	def sub_encrypt(text, key, alphabet):
		map = str.maketrans(alphabet, key)
		return text.translate(map)
	#print(text)
			
def hash_file(path, algorithm = 'md5', size = 65536):
	try:
		hash = hashhlib.new(algorithm)
		with open(path, 'rb') as f:
			while true:
				s = f.read(size)
				if not s:
					break
				hasher.update(s)
		return hasher.hexdigest()
	except fileNotFound:
		print(f"Error: File not found at {file_path}")
		return None
	except valueError:
		print(f"Error: Invalid hashing algorithm' {algorithm}' specified.")
		return None 
		
def decrypt(text, key):
	def de_transposition(text, key):
		num_column = len(key)
		num_row = (len(ciphertext) + num_column -1)
		
		grid = [['' for _ in range(num_columns)] for _ in range(num_row)]	
		cipher_index = 0
		for column_index in key_sort_index:
			for r in range(num_rows):
				grid[r][column_index] = ciphertext[cipher_index]
				cipher_index +=1
		plaintext =[]
		for r in range(num_rows):
			for c in range(num_column):
				plaintext.append(grid[r][c])
		return "".join(plaintext).rstrip
	def de_substitution(text, key, alphabet):
		map = str.maketrans(key, alphabet)
		return text.translate(map)

def decrypt_file(input_file, output_file, key):
	try:
        with open(input_file, 'r') as file:
            	lines = file.readlines()	
		            
        with open(output_file, 'w') as file:
            	for line in lines:
                	file.write(decrypt(line, key))
    	#except FileNotFoundError:
        #	print(f"Error: {input_file} not found!")

        	
if __name__ == "__main__":
	print("1. Encrypt a file")
	print("2. Decrypt a file")
    
	choice = int(input("Enter your choice: "))
	input_file = input("Enter the input file name: ")
	output_file = input("Enter the output file name: ")
	key = input("Enter the encryption/decryption key (integer): ")

	if choice == 1:
        	encrypt(input_file, output_file, key)

	elif choice == 2:
        	decrypt_file(input_file, output_file, key)
	else:
		print("Invalid choice.")		
		
		
				
