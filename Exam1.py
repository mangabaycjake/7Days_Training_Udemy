alpNumCharSet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
print("String checker. Enter blank to exit")
Cont = True
while Cont:
	inputString = input("Write your alphanumeric string : ")
	if inputString == "":
		print("You have exited")
		Cont = False
	else:
		isAlpNum = Truea
		for a in inputString:
			if not (a in alpNumCharSet):
				print(f"Sorry, your string {inputString} is not made solely of alphanumeric characters.")
				isAlpNum = False
		if isAlpNum:
			print(f"Nice, your string {inputString} is made of alphanumeric characters.")
		
