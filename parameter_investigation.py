# parameter_investigation.py

# greeting now has a default value of Welcome
def greet(name, greeting="Welcome", times=1):
    for i in range(times):
        print (f"{greeting} {name}")

greet("Alice", "Welcome")
greet("Bob", "Failte")

# named parameters / keyword parameters
greet(name="Carol", greeting="Wilkommen")
greet(greeting="Bienvienu", name="Dan")

greet("Eve", times=3)

# using named parameters with sensible defaults really simplifies
# calling complex function in matplotlib









