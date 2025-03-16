# Write a Python program to find the largest among three numbers using if...elif...else.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1 > num2 and  num1 > num3:
    print("num1 is large.")
elif num2 > num1 and num2 > num3:
    print("num2 is large.")
else:
    print("num3 is large.")