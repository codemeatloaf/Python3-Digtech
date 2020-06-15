# 2.	Write a Python function to check whether a number is divisible by another number.
# Accept two integer values from the user

a = int(input("Input first number here: "))
b = int(input("input second number here: "))

# this is defining the multiples of 'A' and 'B', if it equals zero or cant multiply them it returns False.

def multiple(a, b):
    return True if a % b == 0 else False
# capitalization is important for False and True!!!
print(multiple(b, a))

# sources:
# https://stackoverflow.com/questions/52773914/fastest-way-to-check-if-a-number-is-divisible-by-another-in-python
# sources:
# https://www.w3resource.com/python-exercises/python-basic-exercise-147.php
