# 6.	Write a Python program to get a list,
# sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
import operator
list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list2 = [(2, 5), (1, 4), (5, 3), (4, 2), (3, 1)]
# Test:
testsorted = sorted(list2)
# This just sorts the first number, not the list in the tuple.
print("Test: ")
print(list2)
print(testsorted)
# Import operator. SUPER IMPORTANT
print("List1: ")
list1.sort(key = operator.itemgetter(0))
print(list1)
# Sources:
# https://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/
# Sources:
# https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index