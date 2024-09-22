print("This program selects even numbers from a list")

def wholeTask():
    try:  # Get number of numbers
        noNumbers = int(input("How many numbers would you like to list?"))
        if 10 > noNumbers > 0:
            # Get list
            numList = []
            evenList = []
            inpNum, i = int(), 1
            while i <= noNumbers:
                try:
                    inpNum = int(input(f"Enter num {i}: "))
                    numList.append(inpNum)
                    if inpNum % 2 == 0:
                        evenList.append(inpNum)
                    i += 1
                except:
                    print("Please try again with valid integer.")
            print(f"In the list {numList}, the even numbers are {evenList}.")
                
        else:
            print("Sorry, please select only 1 to 10 for simplier task.")
            wholeTask()
    except:
        print("Sorry, please select only 1 to 10 for simplier task.")
        wholeTask()
wholeTask()