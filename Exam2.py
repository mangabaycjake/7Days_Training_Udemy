print("\\")
while True():
	print("el")

Cont = True
print("Previous and Next number indicator. Enter blank to exit.")
while Cont:
	inputNumber = input("Please input your integer: ")
	if inputNumber == "":
		print("You have exited.")
		Cont = False
	else:
		# Check if integer
		try:
			inputNumber = int(inputNumber)
			print("Previous number: " + str(inputNumber - 1))
			print("Next number: " + str(inputNumber + 1))
		except:
			print("Please input a valid integer number only!")
			

