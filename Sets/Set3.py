# 3.	Write a Python program to add member(s) in a set
# Define the set
set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
lst = list(set1)
lst2 = list.copy(lst)
# You can't copy a set, so turn it into a list and copy it.
lst2.append(10)
lst2.append(11)
lst2.append(12)
# After you have added the new things to the list, turn it back to a set.
set2 = set(lst2)
# Just to tell if it worked, and now there is a copy of set1
print("This is the first set: ", set1)
print("This is the copy of the set: ", set2)
