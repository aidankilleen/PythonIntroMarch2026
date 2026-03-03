# datetime_investigation.py

from datetime import datetime

dt = datetime.now()

print(dt)

print(dt.day)
print(dt.month)
print(dt.year)

jan1 = datetime(2026, 1, 1)

print (jan1)

print (dt - jan1)

if jan1 < dt:
    print ("we are after jan1")

