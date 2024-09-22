# Exercise 1
StartNum = int(input("Input your start number: "))
EndNum = int(input("Input your end number: "))

# For
for i in range(StartNum, EndNum + 1):
	print(i)
	

# While
a = StartNum
while not (a > EndNum):
	print(a)
	a += 1
