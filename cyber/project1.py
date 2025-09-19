#import os
alphabets = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(text, key):
	encrypted_text = ''.join([chr(ord(char) + key) for char in text])
	for char in text:
    		try:
    			i = (alphabets.index(char) + key) % 26
    			results += alphabets[i]
    		except Error:
    			results += char
    			return results.lower()  
    		return encrypted_text

def decrypt(text, key):
	decrypted_text = ''.join([chr(ord(char) - key) for char in text])
	for  char in text.lower():
		try:
    			i = (alphabets.index(char) - key) % 26
    			results += alphabets[i]
    	except Error:
    		results += char
    		return results.lower()
    	return decrypted_text

def encrypt_file(input_file, output_file, key):
	try:
        	with open(input_file, 'r') as file:
            		lines = file.readlines()
 	    		for lines in input_file:
            			encrypted_text = encrypt(text, key)
            			outfile.write(encrypted_text)     
       		with open(output_file, 'w') as file:
            		for line in lines:
                		file.write(encrypt(line, key))
                
	except FileNotFoundError:
		print(f"Error: {input_file} not found!")
    

def decrypt_file(input_file, output_file, key):
	try:
        	with open(input_file, 'r') as file:
            		lines = file.readlines()
            		for lines in input_file:
            			decrypted_text = decrypt(text, key)
            			outfile.write(decrypted_text)	
		            
        	with open(output_file, 'w') as file:
            		for line in lines:
                		file.write(decrypt(line, key))
    	except FileNotFoundError:
        	print(f"Error: {input_file} not found!")
    

if __name__ == "__main__":
	print("1. Encrypt a file")
	print("2. Decrypt a file")
    
	choice = int(input("Enter your choice: "))
	input_file = input("Enter the input file name: ")
	output_file = input("Enter the output file name: ")
	key = int(input("Enter the encryption/decryption key (integer): "))

	if choice == 1:
        	encrypt_file(input_file, output_file, key)
	elif choice == 2:
        	decrypt_file(input_file, output_file, key)
    	else:
        	print("Invalid choice.")
        
        
        
        
        
        
        
        
        
        
        
        
