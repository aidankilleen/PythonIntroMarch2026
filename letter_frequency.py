# letter_frequency.py

s = "aaaa abc dAAA!!£$%^"

# how many of each letter?

# iterate through each letter in the string
# for i in range(len(s)):
#    print (f"{i} {s[i]}")

# logically consistent python means 
# if I can iterate through the items in a list
# the keys in a dictionary
# why no the letters in a string?

letter_counts = {
}
discarded = 0
for letter in s:
    if letter.isalpha():
        if letter.lower() in letter_counts:
            # increment the letter count
            letter_counts[letter.lower()] += 1
        else:
            # initialise the letter count
            # first time encountering this letter
            letter_counts[letter.lower()] = 1
    else:
        discarded += 1
print (letter_counts)
print (f"discarded:{discarded}")

for letter in letter_counts:
    print (f"{letter}", "*" * letter_counts[letter], sep="\t")




