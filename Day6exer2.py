print("This program gives the square of numbers starting from number 'a' increasing 1 by 'a' number of times")

a = int(input("Input your number: "))

for i in range(a, a + a):
	print(f"{i} * {i} = {i * i}")

print("-----------")
b = a
while b < 2 * a:
	 print(str(b) + " * " + str(b) + " = " + str(b * b))
	 b += 1
