# list_intro.py

# don't call your variable "list"
# list = [1,2,3,6,5,4]


numbers = [9, 5, 3, 2, 6, 1, 8]

print (numbers)

print (numbers[1])  # NB: list index starts at 0 numbers[1] is the second item
print (numbers[0]) # numbers[0] is the first item

print (len(numbers))

# print (numbers[7]) # index 7 is invalid for a list with 7 items 0-6 are valid

# pythonic - you can use a negative index
print (numbers[-1]) # -1 is the last item

# you can detect if an item is in the list
if 2 in numbers:
    print ("2 is in the list")
else:
    print ("2 is not in the list")

# iterate the items in a list
for number in numbers:
    print (number)

message = "this is a some sort of message"
words = message.split()

for word in words:
    print (word)



































