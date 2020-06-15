# 9. Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

x = int(input("Please enter your first number here: "))
y = int(input("Please enter your second number here: "))
z = int(input("Please enter your third number here: "))


def sum_thrice(x, y, z):
    sum = x + y + z
# Return sum is real important, dont forget it again lol
    if x == y == z:
        sum = sum * 3
        return sum

# 1 + 2 + 3 isn't working but 3 + 3 + 3 is??????
print(sum_thrice(x, y, z,))
