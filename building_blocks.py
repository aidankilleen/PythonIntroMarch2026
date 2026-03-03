# building_blocks.py
# By: Aidan
# Date: 2/3/2026

# Building Block #1 - comment


# Building Block #2 - variables
x = 10
name = "Aidan"
f = 1.2
n = 99

# python is weakly typed - it is possible to change the type
n = "ninety nine"


# Building Block #3 - expressions
a = 10
b = 20


answer = a + b * 100 / 2 + 2 ** 3

# order of precedence is PEMDAS
# Parenthesis ()
# Exponents
# Multiplication
# Division
# Addition
# Subtraction

# strongly recommend just using brackets
answer = (a + ((b * 100) / 2)) + 2 ** 3

# two shortcuts:
# <alt> down arrow - will copy a line
# <alt> up or down will move a line

# pythonic - this is something that is unique or particular to python
# 

# you can multiply a string in python

print ("*" * 50)


# Building Block 4

# loop
# nb: in python the tab (indent) is required and part of the syntax
count = 1

while count <= 10:
    print (count)
    #count = count + 1
    count += 1

    # python does not support count++ syntax

# for loop
print ("for loop:")
for i in range(5):
    print (i)

# Building Block # 5
# conditions

a = 10

if a > 5:
    print ("a is greater than 5")
elif a > 10:
    print ("a is greater than 10")
else:
    print ("a is less than 5")


# inline conditionals
# pythonic - other languages use different syntax
a = 1
message = "big" if a > 10 else "small"

print ("the value is", message)


# Building Block # 6 - functions
print("this is a message")

print (len(message))

# there 50 or so built-in functions 
# the python standard library is very comprehensive
# there are 3rd party libraries as well 

# we will be creating our own functions:
def greet(name):
    print ("Welcome", name)

greet("Alice")
greet("Bob")
greet("Carol")
greet("Dan")


# Building Block # 7 - [array] - lists
names = ["Alice", "Bob", "Carol", "Dan"]

# create a new variable called "name"
# and use that to iterate the items in the list
for name in names:
    greet (name)

# lists have a huge number of uses in python
# python has a few different types of list (data structures)

# Building Block #8 - Objects
# (almost) everyting in python is an object

message = "this is a message"

print (message)
print (message.upper())

# in programming
# an object has value(s) and function(s) in a reusable unit
# pressing . will show all of the properties and functions in an object

i = 99
f = 99.9

# we will often get objects from modules
# but we will also be creating our own objects

# python is a fully Object Oriented Programming Language

print (message.title())






































print ("finished")












