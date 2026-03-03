# set_investigation.py


# data structures in python:
# list
# tuple
# dictionary
# set

# square brackets -> list
names = ["Alice", "Bob", "Carol", "Alice", "Dan", "Carol", "Dan", "Carol"]
print (names)

# curly brackets here -> set
# a set is a list with no duplicate items - each item can only be added once
names = {"Alice", "Bob", "Carol", "Alice", "Dan", "Carol", "Dan", "Carol"}
print (names)
names.add("Eve")

print (names)
names.add("Alice")
names.add("Bob")
names.add("Carol")
print (names)

# having unique lists is useful for a lot of data processing operations

list1 = ["red", "green", "blue", "orange", "purple"]
list2 = ["green", "orange", "black", "white", "purple"]

unique_list = set(list1 + list2)

print (unique_list)

# there are set operators in python

s1 = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4}
s2 = {2, 2, 2, 4, 5, 6}

print (s1)
print (s2)

print (s1 | s2) # union operator - s1 or s2 
print (s1 & s2) # intersection operator s1 and s2
print (s1 - s2) # difference - items in s1 that are not in s2
print (s2 - s1) # difference - items in s2 that are not in s1
print (s1 ^ s2) # symmetric difference - items that are not common

# we can use < to check if a set is a subset 

s1 = {1,2,3,4,5,6,7,8}
s2 = {2, 4, 6, 8}

if s2 < s1:
    print ("s2 is a subset of s1")
else:
    print ("s2 is not a subset of s1")

s2.add(99)    

if s2 < s1:
    print ("s2 is a subset of s1")
else:
    print ("s2 is not a subset of s1")



















