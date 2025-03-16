# WAP to create a user define function and perform separate arithmetic Operator.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

def operator(num1, num2):
    add = num1 + num2
    print(f"Addition: {num1} + {num2} = {add}")
    sum = num1 - num2
    print(f"Subtraction: {num1} - {num2} = {sum}")
    mul = num1 * num2
    print(f"Multiplication: {num1} * {num2} = {mul}")
    div = num1 / num2
    print(f"Division: {num1} / {num2} = {div}")
    mod = num1 % num2
    print(f"Modulus: {num1} % {num2} = {mod}")

operator(num1, num2)