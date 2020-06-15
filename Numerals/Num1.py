
# 1. Write a Python program to check whether a variable is an integer or string.

a = input("Input a number or word here: ")
if type(a) == str:
    print("This is a string")
else:
    int(a)
    print("This is something else")

# This one works so far

# Sources: https://note.nkmk.me/en/python-check-int-float/
# Sources: https://pythonprinciples.com/blog/check-if-var-is-string/