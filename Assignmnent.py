listDays = ["Sunday", "Monday", "Tuesday" ,"Wednesday","Thursday", "Friday", ""]
listDays[6] = "Saturday"
tupleDays = tuple(listDays)
print(tupleDays)

yearx = int(input("Input your birth year: "))
monthx = int(input("Input your birth month number: "))
dayx = int(input("Input the day of your birthday: "))

dayOld = 20 - dayx
monthOld = 9 - monthx
yearOld = 2024 - yearx

if dayOld < 0:
	febDays = 28
	if yearx % 4 > 0:
		febDays = 29
	noDaysInMonth = [31, febDays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	dayOld += noDaysInMonth[monthx - 1]
	monthOld -= 1
	
if monthOld < 0:
	monthOld += 12
	yearOld -= 1
	
if yearOld >= 0:
	print(f"You are {yearOld} years, {monthOld} months,and {dayOld} days old.")
else:
	print("Are you a time traveller?")

