# 8.	Write a Python program to check a list is empty or not.
# This one isn't all that hard
x = input("Input a string, or just press enter to leave it empty: ")
if len(x) == 0:
    print("This list is empty.")
else:
    print("This list is not empty.")
# This explains itself, but it checks if the length of the string is 0, if it is it is shown as empty. If not,
# It prints "This line is not empty."
