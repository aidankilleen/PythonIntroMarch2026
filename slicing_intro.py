# slicing_intro.py

# slicing is unique to python (pythonic)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print (len(numbers))
print (numbers[0])
print (numbers[-1])

# [start:stop] - notice start is inclusive and stop is exclusive
print (numbers[1:4])

print (numbers[:4]) # leave out the start assumes 0
print (numbers[4:]) # leave out the stop assumes the end
print (numbers[:])  # start to end - why??????

# [start:stop:step]
print (numbers[1:8:2])
print (numbers[::2])

# using a negative step reverses list
print (numbers[::-1])

# slicing works for any kind of list
names = ["Alice" ,"Bob", "Carol", "Dan", "Eve", "Fred"]

print (names)
print (names[::2])
print (names[1::2])













