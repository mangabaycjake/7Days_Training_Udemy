

# Total of marks
def sumTheMarks(mark1, mark2, mark3):
	sumOfMarks = mark1 + mark2 + mark3
	print(f"Total Marks: {sumOfMarks}")
	return sumOfMarks

# Average of Marks
def aveTheMarks(mark1, mark2, mark3):
	aveOfMarks = (mark1 + mark2 + mark3) / 3
	print(f"Average: {aveOfMarks}")
	return aveOfMarks

# Take three subject marks
def take3marks():
	Mark1 = int(input("Input 1st mark: "))
	Mark2 = int(input("Input 3nd mark: "))
	Mark3 = int(input("Input 3rd mark: "))
	sumMark = sumTheMarks(Mark1, Mark2, Mark3)
	aveMark = aveTheMarks(Mark1, Mark2, Mark3)

# START
take3marks()



