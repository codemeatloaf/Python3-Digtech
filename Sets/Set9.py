# 9.	Write a Python program to create a symmetric difference
set1 = {"google, bing, gibiru"}
set2 = {"google, firefox, yahoo"}
print("The first set: ", set1)
print("The second set: ", set2)
# Set 3 is the name of the object, and the object consists of set1 ^ set2.
# ^ is 'symmetric difference'
set3 = set1 ^ set2
print("The symmetric differece between", set1, "and", set2, "is", set3)

