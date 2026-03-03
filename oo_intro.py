# oo_intro.py

# string is an object
# most things in python are objects as well
from user import User

name = "Alice"
#print (name)
#print (name.upper())

numbers = [1,6,4,32,5]

u = User(99, "Yvonne", "yv@gmail.com", True)

u.display()

# creating an object - creates a new data type
# this data type should behave like all other data types

numbers = [1,2,3]

users = [
    User(1, "Alice", "alice@gmail.com", True),
    User(2, "Bob", "bob@gmail.com", False),
    User(3, "Carol", "carol@gmail.com", True),
    User(4, "Dan", "dan@gmail.com", False),
    ]


for user in users:
    print (user.name)

print (users[-1].email)

print (users[2:])

active_users = [user for user in users if user.active]

for user in active_users:
    user.display()

u = User(99, "Zoe", "zoe@gmail.com", True)

print (u)


print (users)





























