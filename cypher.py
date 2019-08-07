import sys
import random

lowerBound = 65
upperBound = 91

printLetters = False
#printLetters = True

if printLetters:
	forwardList = [chr(i) for i in range(lowerBound,upperBound)] # uppercase
	for i,f in enumerate(forwardList):
		print(ord(f),i+1,f)

def encrypt(plainText, key):
	global lowerBound
	global upperBound
	retStr = ""
	code = plainText.upper()
	#print(code)
	for c in code:
		if c == ' ':
			retStr += ' '
			continue
		charNumber = ord(c)
		sum = charNumber + key
		#print("encryptSUM",sum)
		if sum > (upperBound-1):
			sum -= (upperBound-lowerBound)
		retStr += chr(sum)
	return retStr

def decrypt(cypherText, key):
	global lowerBound
	global upperBound
	retStr = ""
	code = cypherText.upper()
	#print(code)
	for c in code:
		if c == ' ':
			retStr += ' '
			continue
		charNumber = ord(c)
		sum = charNumber - key
		if sum < lowerBound:
			sum += (upperBound-lowerBound)
		retStr += chr(sum)
	return retStr
	
def main(plainTxt, key):
	cypher = encrypt(plainTxt,key)
	
	print(cypher)
	print(decrypt(cypher,key))

if __name__ == "__main__":
	print(len(sys.argv))
	if len(sys.argv) == 2:
		plainTxt = "TEST"
		key = int(sys.argv[1])
		with open(".\key.txt", "w") as f:
			f.write(str(key))
			f.write("\n")
		main(plainTxt, key)
	if len(sys.argv) == 3:
		plainTxt = str(sys.argv[1])
		key = int(sys.argv[2])
		with open(".\key.txt", "w") as f:
			f.write(str(key))
			f.write("\n")
		main(plainTxt, key)
	else:
		plainTxt = "TEST"
		key = random.randrange(1,10)
		with open(".\key.txt", "w") as f:
			f.write(str(key))
			f.write("\n")
		main(plainTxt, key)
