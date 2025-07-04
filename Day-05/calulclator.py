
import sys 
import os

def add(num1,num2):
    add=num1+num2
    return add 

def sub(num1,num2):
    sub=num1-num2
    return sub 

num1 = float(sys.argv[1])
opeartion = sys.argv[2]
num2 = float(sys.argv[3])

if opeartion == "add":
    print(add(num1,num2))

if opeartion == "sub":
    print(sub(num1,num2))


print(os.getenv("password"))



