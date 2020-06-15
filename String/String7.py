# 7.	Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.


# the line 'def' is used to define a function, so by putting 'def verbing(a)' it is defining the verbage of 'a'
# _____.endswith is asking the computer if the word has "ing" at the end, if it does it will continue with the code
# I couldnt get it to work with the code, su i used [-3] instead

def add_string(a):
    length = len(a)
    if length > 2:
        if a[-3:] == ("ing"):
            a += 'ly'
        else:
            a += 'ing'

    return a


print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))

# sources: https://www.w3schools.com/python/python_conditions.asp
# sources: https://stackoverflow.com/questions/2485378/pythonic-way-of-adding-ly-to-end-of-string-if-it-ends-in-ing
# sources: https://www.codecademy.com/forum_questions/5455392252f8631c950028c1
