## This iteration of the READER file will also sort the Text file, and then print it

names = []

## "r" is the default, and does not need to be specificed)
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

## this will sort in descending order, from Z to A
for name in sorted(names, reverse=true):
    print(f"hello, {name}")

