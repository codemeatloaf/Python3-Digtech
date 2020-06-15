# 5.	Write a Python program to remove an item from a set if it is present in the set.

set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1)
a = int(input("Input a number from the set above, and input it here: "))
# The input is the number we will be discarding with .discard.
set1.discard(a)
print(set1)
