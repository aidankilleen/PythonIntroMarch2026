# fileio_investigation.py

fp = open("test.txt")

lines = fp.readlines()

print (lines)

for line in lines:
    print (line, end="")

fp.close()


# file output
fp = open("newfile.txt", "w")
fp.write("Is this working?")
fp.close()

print ("\n", "*" *50)
# you can automatically have your file closed using "with"

with open("test.txt") as fp:

    first_line = fp.readline()
    print (first_line)

    #for item in fp:
    #    print (item, end="")

    lines = fp.readlines()
    print (lines)

# fp is automatically closed when we get to here

print ("Finished")





