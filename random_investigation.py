# random_investigation.py
from random import randint

r = randint(1,10)

# modify this to have 3 conditions
# <5 is small <8 is medium else large
print (f"{r} is {"small" if r < 5 else "large"}")

if r <5:
    print (f"{r} is small")
elif r < 7:
    print (f"{r} is medium")
else:
    print (f"{r} is large")

print (
    f"{r} is {"small" if r < 5 else "medium" if r < 7 else "large"}")

# category = "small" if r < 5 elif r < 7 "medium" else 














