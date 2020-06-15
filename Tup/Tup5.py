# 4.	Write a Python program to unpack a tuple in several variables.
tpl = [1, 2, 3, 4, 9, 8, 7, 6, 5]
tpl2 = tpl.copy()
lst = list(tpl2)
# Append means add, but you need to turn it into a list first.
# Remember to turn it back to a tuple afterwards

lst.append(2020)
tpl2 = tuple(lst)
print(tpl2)
# I'm trying to make the names of the objects easier to type

