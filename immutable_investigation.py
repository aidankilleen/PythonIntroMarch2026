# immutable_investigation.py


numbers = [4, 2, 1, 6, 4, 7, 10, 9]
print (numbers)

# lists are mutable - they can be changed
numbers[0] = 999

print (numbers)

numbers = [4, 2, 1, 6, 4, 7, 10, 9]
cp = numbers    # not a copy!!!! the two variables are referring to the same list

# sometimes referred to as a clone of the list

print (numbers)
print (cp)

numbers[0] = 999

print (numbers)
print (cp)


numbers = [4, 2, 1, 6, 4, 7, 10, 9]
cp = numbers[:] # this is a copy of the list

print (numbers)
print (cp)

numbers[0] = 999

print (numbers) # first list has changed
print (cp)      # second list has not


numbers = [4, 2, 1, 6, 4, 7, 10, 9]
cl = numbers
cp = numbers[:]

# use id() to get the unique id of the object - (looks like a memory address)
print (id(numbers))
print (id(cl))
print (id(cp))

# strings are immutable in python!
# each assignment to a string creates a whole new string object
name = "Aidan"
print (id(name))
name += " "
print (id(name))
name += "Killeen"
print (id(name))

print (name)

name = "alice"
print (name)
print (id(name))
print (name[0])
#name[0] = "A"   # you cannot modify a string once it's been created

# we can create a new string object using slicing
name = name[0].upper() + name[1:]

print (name)
print (id(name))

# most things in python are actually immutable
# list and dictionaries are mutable, most other things are not
i = 99
print (f"{i} - {id(i)}")
i += 1
print (f"{i} - {id(i)}")





































