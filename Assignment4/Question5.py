print("This program reverses the order of words")

inpString = str(input("Write your string: "))

# Method 1: Using split
divString1 = inpString.split(' ')

revString1 = str()
for word in divString1:
    revString1 = word + " " + revString1

print(f"Reversed string using method 1: {revString1}")

# Method 2: Long method
word2, revString2 = str(), str()
for charac in inpString:
    if charac != ' ':
        word2 += charac
    else:  # if space
        revString2 = word2 + " " + revString2
        word2 = ""
revString2 = word2 + " " + revString2

print(f"Reversed string using method 2: {revString2}")
