# WAP to pass a,b argument in class function and return the value of Class Function.

class Calculation:
    def add(self, a, b):
        return a + b

num1 = int(input("Enter a num1: "))
num2 = int(input("Enter a num2: "))
C = Calculation()
    
print("Addition: ",C.add(num1,num2))