taskName = "Sum of 1 to N"

print("This program calculates " + taskName)

def task():
    try:
        inputNumber = int(input("Enter a positive integer: "))
        if inputNumber > 0:
            sum = 0
            for i in range(1, inputNumber + 1):
                sum += i
            print(f"The sum of numbers from 1 to {inputNumber} is {sum}")
        else:
            print("Sorry, please input integer greater than 0.")
            task()
    except:
        print("Please input a valid integer.")
        task()

task()
