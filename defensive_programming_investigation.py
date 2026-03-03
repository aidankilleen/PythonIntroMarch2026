# defensive_programming_investigation.py
response = input("Enter a number")

# defensive programming 
# write code to check all inputs
if not response.isnumeric():
    print ("enter a number next time")
    exit()

n = int(response)

for i in range(n):
    print (f"{i}")


print("finished")

# this works but can be very complex and difficult as the application grows in size