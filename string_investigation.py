# string_investigation.py
# lower case + underscores are used for naming in python

message = "String Investigation"
print (message.title())

a = 10
b = 20

answer = a + b

# you can't add a number to a string
# but str() built in function converts (almost) anything to a string
print ("the answer is " + str(answer))

print (str(a) + " + " + str(b) + " = " + str(answer))

# there is a better way:

# f - string
# you can substitute variables into strings using {}
# no need for str() function in an f-string
print (f"{a} + {b} = {answer}")

# you can substite in an expression
print (f"{a} + {b} = {a+b}")


# escape sequences begin with \
name = "Alice O'Reilly"
message = "press the \"red\" button"
print (message)

# \n = newline
# \t - tab
# \r = carriage return
# \" = quotation mark
# \\ = single \ character

filename = "c:\\my documents\\files\\myfile.txt"
print (filename)


# multiline strings
message = """
    this is
    a multi line
    string
"""

print (message)

calculation = f"""
    {a}
+   {b}
---------
    {a+b}
"""

print (calculation)

# use the same to create a multiline comment
"""
This 
is
a
multiline
comment
"""





























































