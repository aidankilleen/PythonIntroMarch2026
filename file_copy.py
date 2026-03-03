# file_copy.py

source = "test.txt"
destination = "copy.txt"

# write the code to copy file source to destination
# open 1 file and write to the second

with open(source) as fp_source:

    #it is usually a bad idea to read the whole file
    lines = fp_source.readlines()


with open (destination, "w") as fp_destination:

    for line in lines:
        fp_destination.write(line)


print (f"Copied {source} to {destination}")

