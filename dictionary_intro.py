# dictionary_intro.py

# a dictionary is a data structure
# containing key-value pairs
# {"key1":value, "key2":value2}

d = {
    "id":1, 
    "name":"Alice", 
    "email": "alice@gmail.com", 
    "active":True
}

print (d)

print (d["id"])
print (d["name"])
#print (d["doesntexist"])    # accessing an item that doesn't exist causes a KeyError

# logical consistency
# If I can iterate through a list as follows
numbers = [1,5,4,3,6]
for number in numbers:
    print (number)

if 5 in numbers:
    print ("5 is in the list")


# what would make sense if I iterate through the items in my dictionary?
for key in d:
    print (f"{key} = {d[key]}")

print (d.keys())
print (d.values())
print (d.items())

# dictionaries are mutable modifiable

d["phone"] = "08712345676"
print (d)

if "phone" in d:
    print (d["phone"])
else:
    print ("no phone")


    
























