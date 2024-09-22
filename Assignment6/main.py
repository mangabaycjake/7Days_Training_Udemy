from add import add_numbers
from subtract import subtract_numbers
from multiply import multiply_numbers
from divide import divide_numbers

try:
    num1 = float(input("1st Number: "))
    num2 = float(input("2ndt Number: "))

    sum = add_numbers(num1, num2)
    print("sum: " + str(sum))

    difference = subtract_numbers(num1, num2)
    print("differnce: " + str(difference))

    product = multiply_numbers(num1, num2)
    print("product: " + str(product))

    quotient = divide_numbers(num1, num2)
    print("quotient: " + str(quotient))
except:
    print("Please input valid numbers.")
