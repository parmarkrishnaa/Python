# WAP to create a two level of Indentation.

num1 = input("Enter a num1: ")
num2 = input("Enter a num2: ")
num3 = input("Enter a num3: ")

if num1 < num2:
    if num1 < num3:
        print(num1, 'is', 'small')
    else:
        print(num3, 'is', 'small')
else:
    if num2 < num3:
        print(num2, 'is', 'small')

    else:
        print(num3, 'is', 'small')