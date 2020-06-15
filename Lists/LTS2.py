# 2.	Write a Python program to multiplies all the items in a list.

# This is the list for numbers to input
a = int(input("Input a number here: "))
b = int(input("Input a second number here: "))
c = int(input("Input a third number here: "))
# It turns them into integers
# This turns integers into a list
list1 = [a, b, c]
# Use list two to make sure the code is working
list2 = [3, 2, 4]

# i is for Iterate, so it multiplies the first number by 1, and then multiplies the first number by the next number
# and so on
# For every i in list1, it multiplies x by the value current list item
x = 1
for i in list1:
    x = x * i
print(x)

# Sources:
# https://www.bbc.co.uk/bitesize/guides/z3khpv4/revision/1#:~:text=An%20explanation%20of%20iteration%2C%20as,is%20the%20process%20of%20repeating
