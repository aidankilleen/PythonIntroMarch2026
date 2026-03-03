# wc.py

# count the lines, words and characters in the specified file
# handle errors gracefully

# usage
# python wc.py FILE

# read command line arguments
import sys


try:
    filename = sys.argv[1]

    with open(filename) as fp:
        lines = fp.readlines()
        word_count = 0
        character_count = 0

        for line in lines:
            character_count += len(line)
            words = line.split()
            word_count += len(words)

        print (f"lines:{len(lines)}")
        print (f"words:{word_count}")
        print (f"characters:{character_count}")

except Exception:
    print ("wc.py")
    print ("Usage:")
    print ("python wc.py FILE")

    exit(-1)

