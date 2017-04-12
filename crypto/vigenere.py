from helpers import alphabet_position, rotate_character

def encrypt(text, key):
	encrypted = ""
	keyindex = []
	keyinititialindex = 0
	for eachchar in key:
		index = alphabet_position(eachchar)
		keyindex.append(index)
		
	
	for char in text:
		if keyinititialindex == len(keyindex):
			keyinititialindex = 0
		if char.isalpha():
			encrypted = encrypted + rotate_character(char, keyindex[keyinititialindex])
			keyinititialindex += 1
		else:
			encrypted = encrypted + char
	return encrypted
	


#print(encrypt('Hello, World!', 5)) 
def main():
	inpMessage = raw_input("Type a message:")
	key = raw_input("Encryption Key:")
	#print(inpMessage)
	print(encrypt(inpMessage, key))
	

if __name__ == '__main__':
    main()
