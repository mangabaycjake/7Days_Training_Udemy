import csv

print("This takes avarage of each column from csv file")

filename = 'Question4.csv'
with open(filename, mode='r') as csvFile:
    fileread = csv.reader(csvFile)
    listNum = list(fileread)

print(f"The {filename} contains {listNum}.")
        
colCount = len(listNum[1])
rowCount = len(listNum)
listAve = list()
for colNo in range(0, colCount):
    colSum = 0
    for rowNo in range(0, rowCount):
        colSum += int(listNum[rowNo][colNo])
    listAve.append(colSum / rowCount)

print(f"The average of each column in {filename} is {listAve}.") 