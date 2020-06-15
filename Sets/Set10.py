# 10.	Write a Python program to issubset and issuperset
# Name the sets, and print them for identification.
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Set1", set1)
set2 = {1, "a", 10, 22 }
print("Set2", set2)
set3 = {1, 2, 3}
print("Set3", set3)
# Print and show if it is, in-fact a subset of set1, set2 or set3.
print("Set2 is a subset of set1: ", set2.issubset(set1))
print("Set3 is a subset of set1: ", set3.issubset(set1))
