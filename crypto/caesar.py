from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
	encrypted = ""
	for char in text:
		encrypted = encrypted + rotate_character(char, rot)
	return encrypted
	


#print(encrypt('Hello, World!', 5)) 
def main():
	inpMessage = raw_input("Type your message:")
	rotate = int(input("Rotate by:"))
	print(inpMessage)
	print(encrypt(inpMessage, rotate))
	

if __name__ == '__main__':
    main()
