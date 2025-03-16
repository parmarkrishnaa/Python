#  Write a program to demonstrate the use of break and continue statements in loops.

for i in range(1, 25):
    if i == 20:
        continue
    
print(i)

for i in range(1, 25):
    if i == 22:
        break
    
print(i)