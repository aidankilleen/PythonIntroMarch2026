

def greet(name: str):
    print (f"Welcome {name}")

# type hints specify what type each parameter is
# and what type the function returns
def message(name: str) -> str:
    return f"Welcome {name}"

m = message("Aidan")

greet("Aidan")
greet(99)