studBasicInfo = {'First Name' : 'Jake', 'Last Name': 'Stone', 'Age': 12, 'Gender' : 'Male', 'ID Number' : 123456}
for k,v in studBasicInfo.items():
	print(f"{k} : {v}")


dictRootSquare = dict()
for i in range(5):
	num = int(input("Please input an integer number #" + str(i + 1) + ": "))
	dictRootSquare[num] = num * num
	
for k,v in dictRootSquare.items():
	print(f"number: {k} : sqaure: {v}")
