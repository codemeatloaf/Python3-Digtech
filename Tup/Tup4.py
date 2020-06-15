# 4.	Write a Python program to unpack a tuple in several variables.
# State the object named tpl, and print the original tpl for reference.
tpl = [1, 2, 3, 4, 9, 8, 7, 6, 5]
print("This is the original tuple.", tpl)
# Give the user the ability to select which integer they want printed from the tuple.
a = int(input("Input the number you wish to select: "))
b = int(input("Input the second number you wish to select: "))
c = int(input("Input the third number you wish to select: "))
# Minus one, because it prints the number selected +1.
print("The first number selected is: ", tpl[a - 1])
print("The second number selected is: ", tpl[b - 1])
print("The third number selected is: ", tpl[c - 1])
