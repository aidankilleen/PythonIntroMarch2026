# cli.py
import sys

print ("CLI")
print (sys.argv)

filename = sys.argv[1]

with open(filename) as fp:
    lines = fp.readlines()
    print (f"There are {len(lines)} in file {filename}")
