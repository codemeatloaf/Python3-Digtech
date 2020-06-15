# 8.	Write a Python program to create the colon of a tuple.
from copy import deepcopy

# create a tuple
a = input("Input a word here: ")
b = int(input("Input a number here: "))

tuplex = (a, b, [], True)
print(tuplex)
# make a copy of a tuple using deepcopy() function
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)

# This is just a copy and paste of the thing from w3resource with the ability to input the things in the tuplex.
# I have zero idea how this works.