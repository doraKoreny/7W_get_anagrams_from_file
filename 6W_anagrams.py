import sys

words = []

if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as my_file:
        for row in my_file:
            words.append(row[:-1])
print(words)
anagram_pairs = {}
for items in words:
    for i in range(len(words)-1):
        if sorted(words[i]) == sorted(items) and words[i] != items:
            print(words[i] + "," + items)