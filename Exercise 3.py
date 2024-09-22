# --------------
# Exercise 3.1: get 5 integer from, store list, display

# Store
integerList = []
integerList2 = []
integerList3 = []
sum = 0
for i in range(0, 5):
    additional = input("Input integer number " + str(i + 1) + ": ")
    integerList.insert(i, int(additional))
    integerList2.extend([int(additional)])
    integerList3.append(int(additional))
print(integerList)
print("List 2: " + str(integerList2))
print("List 3: " + str(integerList3))

for x in integerList:
    sum += x
print(f"Sum: {sum}")

#-----------------------
# Exercise 3.2: "" in a tuple, multiply to each other

integerList = list()
for i in range(0, 5):
    additional = input("Input integer number " + str(i + 1) + ": ")
    integerList.extend([int(additional)])
integerTuple = tuple(integerList)
print(integerTuple)

product = 1
for x in integerTuple:
    product *= x

print(f"Product: {product}")

#------------------------------------
# Exercise 3: set, add

integerSet = set()

for i in range(0, 5):
    additional = input("Input integer number " + str(i + 1) + ": ")
    integerSet.add(int(additional))
print(integerSet)

sum = 0
for x in integerSet:
    sum += x
print(f"Sum: {sum}")
