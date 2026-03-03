# tuple_investigation.py

t = (1, 4, 3, 2, 6, 5, 10, 8, 9)

print (t)
print (len(t))
print (t[0])
print (t[-1])
print (t[3:6])
print (t[:5])
print (t[5:])
print (t[::2])
print (t[::-1])

# you can add two tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)

t = t1 + t2
print (t)

# tuple is immutable, read only, you can't change the contents of a tuple
# t[0]= 999

# why is immutability such a big deal in the python world?

# answer 1 - if python knows something isn't going to change it can optimise the memory
# there is a lot of optimisation built into python based around knowing things
# aren't going to change

# answer 2 - there are strong software engineering quality improvements in knowing 
# something isn't going to just be changed 
# making things immutable eliminates a lot of potential issues and can improve
# quality of the software


# what use is a tuple?

# usecase 1
# return multiple values from a single function
# using an immutable tuple prevents side-effects

def process_list(numbers):
    mx = max(numbers)
    mn = min(numbers)
    return (mx, mn)

values = [1, 4, 3, 2, 5, 6, 9, 8]

answer = process_list(values)

print (f"The answer is {answer}")
print (f"max:{answer[0]}")
print (f"min:{answer[1]}")


# usecase 2 - tuples are useful for multiple assignments and destructuring

a = 1
b = 2
c = 3
d = 4

(a, b, c, d) = (1, 2, 3, 4)

print (f"a = {a}")
print (f"b = {b}")
print (f"c = {c}")
print (f"d = {d}")


(mx, mn) = process_list(values)

print (f"min={mn}")
print (f"max={mx}")

# NB: don't use names of built-in functions as variables!!!
# (max, min) = process_list(values)
# print (max(1, 2, 3))

# usecase 3
# swap two (or more) variables

a = 10
b = 29


print (f"a={a} b={b}")

# this doesn't work because you've overwritten a
#a = b
#b = a

# traditionally you needed to have a temporary variable to do the swap
t = a
a = b
b = t

print (f"a={a} b={b}")

# using a tuple you can do the swap with no temporary
(a, b) = (b, a)

print (f"a={a} b={b}")


d = {
    "id":1, 
    "name":"Alice", 
    "email": "alice@gmail.com",
    "active": True
}

# d.items() returns a list of tuples
print (d.items())

for item in d.items():
    print (item)

# why not extract the key and value from the tuple?
# this is a very pythonic way of doing this?
for (key, value) in d.items():
    print (f"{key}={value}")

# Note - you don't always need the round brackets
t = 1, 2, 3, 4
print (t)

for key,value in d.items():
    print (f"{key}={value}")

print (f"a={a} b={b}")
a,b = b,a
print (f"a={a} b={b}")

# Note - you can create a tuple with a single item
t = (1) # this is not a tuple
print (t)

t = (1,)    # this is a tuple
print (t)

# the uses for immutable lists that contain a single item are few - but they do exist




















































