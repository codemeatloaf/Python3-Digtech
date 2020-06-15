# 7. Write a Python program to remove duplicates from a list.

x = [1, 2, 3, 4, 5, 6, 2, 4, 1, ]
y = [(1, 2), (1, 2), (2, 3,), (4, 5)]

# This creates a dictionary, and uses the list items as keys, and because there can't be duplicates of keys it
# deletes the second ones.
x = list(dict.fromkeys(mylist))
y = list(dict.fromkeys(mylist))

print("List one, with duplicates removed: ")
print(x)
print("List two with duplicates removed: ")
print(y)
# I put the second list just to see how it works
# It removes the dups in the second list!

# Sources: https://www.w3schools.com/python/python_howto_remove_duplicates.asp
