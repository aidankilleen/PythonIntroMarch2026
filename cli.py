# cli.py
import sys

print ("CLI")
print (sys.argv)

filename = sys.argv[1]

try:
    with open(filename) as fp:
        lines = fp.readlines()
        print (f"There are {len(lines)} in file {filename}")
except Exception:
    print (f"Can't open file {filename}")

    