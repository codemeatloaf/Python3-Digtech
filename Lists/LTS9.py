# 9.	Write a Python program to clone or copy a list.
lst1 = [1, 2, 3, 4, 9, 8, 7, 6, 5]
lst2 = lst1.copy()
# .copy and .remove is super useful. They do what they say they do.
lst2.remove(1)
lst2.remove(9)
lst2.remove(5)

print("Old list is: ", lst1)
print("New list with 1, 9 and 5 removed is: ", lst2)

# Sources:
# https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
