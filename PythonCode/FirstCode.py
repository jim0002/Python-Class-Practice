'''
print('Lets Go')
print("Jamin Rahman Jim \n Go for it")
#jamin rahman jim
'''
'''
gdgehbhbrxnh

'''

'''
print("\"Jamin Rahman Jim\"")
name="Jim"
age=21
print("My name is \""+name+"\"")
print("My name is "+name+" and my age is",age,"years")
'''

'''
To connect 2 string or to add any string type variable we will use '+'
But for adding integer or float type variable we have to use ',variable,'

'''

'''
print("My age is", age)
print("My name is",name)

a=10
b=7

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

print(a//b) #it will give us the floor value.

print(a**b) #To the power function.

#Taking input from user

CGPA= input("Enter your CGPA: ")
print("Your Given CGPA is: ",CGPA)

# Type casting

num1= input("Enter First Number: ")
num2= input("Enter Second number: ")
result= int(num1)+int (num2)
print("Result is: ",result)
# another way
num3= int (input("Enter First Number: "))
num4= int (input("Enter Second number: "))
result= num3+num4
print("Result is: ",result)
'''

'''

# Library Function

from math import *  # This function are stored in math library

print(max(20,10))
print(min(20,10))
print(abs(-4))
print(sqrt(4))
print(pow(2,3))
print(round(3.2))
print(round(3.8))
print(floor(3.7))
print(ceil(3.7))


num =20
print(type(num))

# formatting string/ showing the value of a variable in string

num5=20
num6=30
print(f"{num5}+{num6}={num5+num6}")

# Removing new line, here [end=""] will remove the new line  
print("Jamin Rahman--",end="")
print("Jim")

'''

# if else

mark = 20
if (mark>=33):
    print("pass")
if (mark<33):
    print("Fail")
# elif

mark = 70
if mark>=90:
    print("A+")
elif mark>=80:
    print("B")
else:
    print("Fail")