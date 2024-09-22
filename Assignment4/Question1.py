# Write a python program that takes user input and prints wether the given number is even or odd
print("Hi, this determines if number is even or odd")

def takeInput():
    try:
        inputNumber = int(input("Input number: "))
        if inputNumber % 2 == 0:
            print(f"Your number, {inputNumber} is even.")
        else:
            print(f"Your number, {inputNumber} is odd.")
    except:
        print("Please input a valid integer")
        takeInput()
    
takeInput()