## Our goal is to properly format the user's name
## We will use Regular Expression (re) to search for, identify patterns, group & capture things together
import re

name = input("What's your name? ").strip()
## . - any character except a newline
## * - 0 or more repetitions
## + - 1 or more repetitions

##  A|B     either A or B
##  (...)   a group
##  (?:...) non-capturing version. AKA, EXCLUDE what is part of this

## Boolean statement that asks only 1 or 0
## re.Search creates a group, starding with an index of 1 (NOT 0)
## The "Groups" are what are in the parenthesis

## The walrus operator allows us to assign something from right to left, AND  as an IF or ELIF question on the same line


## The walrus operator ":="  combines the following two lines:
# matches = re.search("^(.+), ?(.+)$", name)
# if matches:

if matches:= re.search("^(.+), ?(.+)$", name)
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")