# greeting now has a default value of Welcome
def greet(name, greeting="Welcome", times=1):
    for i in range(times):
        print (f"{greeting} {name}")


if __name__ == "__main__":

    # this code only gets executed if the module is run directly
    # ths code does not get executed if the module is imported
    print (f"__name__:{__name__}")

    greet("Alice")
    greet("Bob", "Failte")
    greet("Carol", times=5)



