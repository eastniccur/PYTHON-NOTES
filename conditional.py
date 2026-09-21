# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age= int(input("Enter your age: "))
print(age)
if age>=18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")

# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 25
your_age = int(input("Enter your age: "))
if my_age > your_age:
    diff= my_age-your_age
    if diff==1:
        print(f"I am {diff} year older than you.")
    else:
        print(f"I am {diff} years older than you.")
elif my_age < your_age:
    diff= your_age-my_age
    if diff==1:
        print(f"You are {diff} year older than me.")
    else:
        print(f"You are {diff} years older than me.")
else:
    print("We are the same age.")

# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
if a>b:
    print(f"{a} is greater than {b}.")
elif a<b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")
