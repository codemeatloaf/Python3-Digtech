# 5.	Write a Python program to count the number of strings where the
# string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

list1 = ['abc', 'xyz', 'aba', '1221']
# List 2 is to show that there are lengths lower then two
list2 = ['ac', 'ai', 'asa', 'amm']
x = 0

# Each bit of the list is an array, it goes 0, 1, -1. minus one is always the last number.
for i in list1:
    if len(i) > 2:
        if i[0] == i[-1]:
            x = x + 1
print(x)
# Indents control whether the code is abiding by if else statements
# == means equality

# List 2 version
x = 0

for i in list2:
    if len(i) > 2:
        if i[0] == i[-1]:
            x = x + 1

print(x)
