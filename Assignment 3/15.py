# Create a nested if condition to check if a person is eligible to vote (age ≥ 18) and is a citizen. 

citizen = input("Are you a citizen(yes/no): ").strip().lower() == 'yes'
age = int(input("Enter your age: "))

if citizen:
    if age >= 18:
        print("You can vote.")
    else:
        print("You cannot vote.") 
else:
    print("You are not citizen you cannot vote.")