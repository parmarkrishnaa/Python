# WAP to create a user define function and perform separate arithmetic Operator.

num1 = ("Enter num1: ")
num2 = ("Enter num2: ")

def operator(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    div = num1 / num2
    mul = num1 * num2
    mod = num1 % num2
    print(f"Addition: {num1} + {num2} = {add}")
    print(f"Subtraction: {num1} - {num2} = {sub}")
    print(f"Division: {num1} / {num2} = {div}")
    print(f"Multiplication: {num1} * {num2} = {mul}")
    print(f"Modulus: {num1} % {num2} = {mod}")

