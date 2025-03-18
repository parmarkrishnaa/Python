# WAP to check if a list is palindrome

list = [6, 9, 6, 9, 6]

list1 = list.copy()

list.reverse()

if list1 == list:
    print("Palindrome")
else:
    print("Not Palindrome")