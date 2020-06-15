# 4.	Write a Python program to remove item(s) from set
set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
lst = list(set1)
lst2 = list.copy(lst)
# This is the same, except instead of .append() it's .remove()
lst2.remove(1)
lst2.remove(3)
lst2.remove(8)
# Turn it back to a set.
set2 = set(lst2)
# Now, there should be removed integers from the first set.
print("This is the first set: ", set1)
print("This is the copy of the set: ", set2)
