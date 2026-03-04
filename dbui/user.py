# user.py
class User:
    def __init__(self, id=-1, name="", email="", active=False):
        # member variables (properties)
        self.id = id
        self.name = name
        self.email = email
        self.active = bool(active)

    def __str__(self):
        # function to convert this object to a string
        return f"{self.id} {self.name} {self.email} {'Active' if self.active else 'Inactive'}"

    def __repr__(self):
        # function to return the debug representaton of the object
        return str(self)

    def display(self):
        print(f"User:{self.id}")
        print(f"{self.name}")
        print(f"{self.email}")
        print("Active" if self.active else "Inactive")

if __name__ == "__main__":
    u1 = User(1001, "Alice", "alice@gmail.com", True)
    u1.display()
    u2 = User(id=1, name="Zoe", email="zoe@gmail.com")
    u2.display()
