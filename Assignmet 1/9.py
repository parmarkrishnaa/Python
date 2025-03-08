# WAP to perform default argument value of sum function.

def sum(a=0, b=0, c=0):
    return a + b + c

res1 = sum(7)
res2 = sum(7, 9)
res3 = sum(7, 10, 11)

print(f"Sum1: {res1}")
print(f"Sum2: {res2}")
print(f"Sum3: {res3}")