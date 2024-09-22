marks = float(input("Your marks: "))

if marks >= 90:
    print("Your grade is A.")
elif marks >= 80:
    print("Your grade is B.")
elif marks >= 70:
    print("Your grade is C.")
elif marks >= 60:
    print("Your grade is D.")
else:
    print("Your grade is Fail.")

# OR

if marks < 60:
    print("Your grade is Fail.")
elif marks < 70:
    print("Your grade is D.")
elif marks < 80:
    print("Your grade is C.")
elif marks < 90:
    print("Your grade is B.")
else:
    print("Your grade is A.")