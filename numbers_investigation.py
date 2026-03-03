# numbers_investigation.py

# normal programming languages use a specific number of bytes to store a number
# python does not do this. There is no maximum number

n = 655362389465234879562378945623987456928374658976234982734982634897263459876
n2 = 239847502834750928347580943098234589023475092834752034975098234750982437509734

print (n * n2)

# not so good at small numbers
# beware there are some rounding issues in floating point numbers
a = 0.1
b = 0.2

answer = a + b

print (answer)

# there are libraries to counteract this deficiency if you need very high precision 
# for small numbers


# other numbers
# python can work with binary numbers directly
a = 0b101100110
b = 0b010011001

print (a)
print (a + b)

print (f"{a:09b}")
print (f"{b:09b}")#
print ("==============")
print (f"{(a+b):09b}")

# bitwise operator
n = 0b10000000

while n > 0:
    print (f"{n:09b}")
    n >>= 1 # shift the binary digits one place to the right

# hex
n = 0xff
print (n)

# oct
n = 0o77
print (n)

# int() can use bases
value = "0xffed"
n = int(value, base=16)
print (f"n={n}")
























