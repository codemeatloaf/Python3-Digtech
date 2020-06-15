# 11.	Write a Python program to clear a set
# Define the set
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Turn the set into a list and copy it
lst = list(set1)
lst2 = list.copy(lst)
# Clear the list then turn it back into a set
lst2.clear()
set2 = set(lst2)
# Print the cleared set and the original set.
print(set1)
print(set2)
