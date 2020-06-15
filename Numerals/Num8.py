# 8. Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input("Enter the number: "))
num = ((abs(1000 - num) <= 100) or (abs(2000 - num) <= 100))

print("Near One Thousand : ", num)

num2 = int(input("Enter a second number: "))
num2 = ((abs(2000 - num2) <= 100) or (abs(1000) <= 100))

print("Near Two Thousand : ", num2)

# Credit for original code: Ravi Kumar
