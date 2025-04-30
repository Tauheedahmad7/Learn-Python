'''name = (input("Enter name :"))

age = int(input("Enter age :"))

print(type(name))
print(type(age))

print(f"My name is {name} and age is {age}")'''


# logical Operator

"""print(12 < 13 and 20 > 15 and 20 < 30 and 21 > 31)

print(12>13 or 21<31 or 34==34)"""


#  Accept two numbers and print the greatest between them.
"""a = int(input("Enter first number : "))

b = int(input("Enter second number : "))

if a > b:
    print("a is greater")
else:
    print("b is greater")"""


"""Q2. Accept the gender from the user as char and print the respective greeting message
 Ex - Good Morning Sir (on the basis of gender)"""

"""gender = input("Enter your gender (M or F):- ")

if(gender=="m" or gender=="M"):
    print("Good Morning Sir")
elif(gender=="f" or gender=="F"):
    print("Good morning Madam")
else:
    print("Wrong character")"""
    

# Accept an integer and check whether it is an even number or odd.
"""
num = int(input("Enter any number :- "))
if(num%2==0):
    print("Even Number")
else:
    print("Odd Number")"""



# Accept name and age from the user. Check if the user is a valid voter or not

"""name = input("Enter your name :-")

age = int(input("Enter your age :-"))

if(age >= 18):
    print(f"Hello {name} you are a valid for vote")
else:
    print(f"Hello {name} you are  not valid for vote ")
"""

# Q5. Accept a year and check if it a leap year or not (google to find out)

year = int(input("Enter any year :-"))

if(year%4):
    print("Leap Year")
else:
    print("Not Leap Year")