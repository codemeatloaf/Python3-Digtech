# 12.	Write a Python program to use of frozensets

set1 = frozenset([1, 2, 3, 4, 5])
set2 = frozenset([6, 7, 8, 9, 10])
set3 = frozenset([3, 4, 5, 6, 7])
# .isdisjointed shows if two sets have nothing to do with eachother.
print("Is the first set disjointed from the second set: :", set1.isdisjoint(set2))
print("Is the first set disjointed from the third set: ", set1.isdisjoint(set3))
print(set1.difference(set2))
print(set1 | set2)

# A frozen set is an immutable version of a set.
# In object-oriented and functional programming,
# an immutable object is an object whose state cannot be modified after it is created
