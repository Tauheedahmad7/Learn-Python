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

"""year = int(input("Enter any year :-"))

if(year%400==0):
    print("Leap Year")
else:
    print("Not Leap Year")"""


# question related to temperature
"""
t =int(input("Enter Temperature :-"))

if(t < 0):
    print("Frezing cold")
elif(t >=0 and t <10):
    print("Very Cold")
elif(t >=10 and t < 20):
    print("Cold")
elif(t >=20 and t<30):
    print("Pleasant")
elif(t>=30 and t<40):
    print("Hot")
else:
    print("Very Hot")"""



# for loop

# a= range(start,stop,step)
 
"""for i in range(-5,-15,-2):
    print(i)"""

# print table of 5
"""n = int(input("Given number of Table :- "))
for i in range(n,n*10+1,n):
    print(i)"""

# a = "Sheryians Coding School"
# print(len(a))
# for i in range(len(a)):
#     print(a[i])

"""a= "SHERYIANS CODING SCHOOL"

for i in a:
    print(i)"""

# for break statement
# for i in range(2,21,2):
#     if(i == 14):
#         break   (break statement me i agr 14 ka value aaya waise hii ruk jayega or aage ka nahi chale ga)
#     else:
#         print(i)

"""for i in range(2,21,2):
    if(i == 14):
        continue   (continue statement me agr i ka value 14 aaya waise hii sirf wo value ko skip krega or baki same to same aayega)
    print(i)"""

# For Loop questions

# 1) Accept an integer and Print hello world n times 

"""n = int(input("Enter any number :- "))

for i in range(n):
    print("Hello World")"""


# 2)  Print natural number up to n 

"""n = int(input("Enter any number you want... "))

for i in range(1,n+1):
    print(i)"""

# 3) Reverse for loop. Print n to 1 
"""
n = int(input("Enter any number..."))

for i in range(n,0,-1):
    print(i)
"""

# 4) Take a number as input and print its table 
"""n = int(input("Enter any number you want to print table :- "))
 for i in range(1,10):
    print(f"{n} * {i} = {n*i}")"""


# 5) Sum up to n terms
n = int(input("Enter number:-"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
    print(f"sum of number is {sum}")