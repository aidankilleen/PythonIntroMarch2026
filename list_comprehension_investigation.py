# list_comprehension_investigation.py

from random import shuffle


names = ["alice", "bob", "carol", "dan", "eve"]

# non pythonic way!
capitalised_names = []

for name in names:
    capitalised_names.append(name.capitalize())

# pythonic way - use a list comprehension
capitalised_names2 = [name.capitalize() for name in names]

print (names)
print (capitalised_names)
print (capitalised_names2)


# use a list comprehension to filter a list
numbers = [1, 3, 2, 4, 5, 6, 9, 7, 10, 8]

odd_numbers = [number for number in numbers if number % 2 == 1]
even_numbers = [number for number in numbers if number % 2 == 0]

print (numbers)
print (odd_numbers)
print (even_numbers)


# use a list comprehension to create the combinations of two lists
products = ["pen", "pencil", "paint", "crayon"]
colours = ["red", "green", "blue"]

product_list = [f"{colour} {product}" for product in products for colour in colours]

print(product_list)


# use the same idea to create a list of all 52 playing cards
# AH, KD, QC, 10S   

# create a list of suits
# create a list of values

# create an array of the combinations of the two

suits = ["H", "D", "C", "S"]
values = ["A"] + [f"{n}" for n in range(2, 11)] + ["J", "Q", "K"]

print (suits)
print (values)

cards = [f"{value}{suit}" for suit in suits for value in values ]

print (cards)

# shuffle the cards
shuffle(cards)

print (cards)

# deal 4 bridge - 13 per hand
hands = [cards[::4],cards[1::4],cards[2::4],cards[3::4]]
print (hands)











































