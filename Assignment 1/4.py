# WAP to declare global variable. 

name = "Global"

def f():
    global name
    name = "Modify"
    print(name)

f()
print(name)