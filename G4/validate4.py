## This tests the RE library
## This library provides the ability to define, check for, and replace patterns.
## https://docs.python.org/3/library/re.html

import re
## re.search(pattern, string, flags=0)
## flags modify the behavior of the function


email = input("What's your email address? ").strip()
## . - any character except a newline
## * - 0 or more repetitions
## + - 1 or more repetitions
## check documentation for more details

## NOTE: the ESCAPE CHARACTER, "\"

## However, this code allows for a full sentence as an entry. Thus, we add a "$" at the end of the code.
## We use "^" to specify the beginning of the entire string of text.
## The user's input must start with this pattern and end with this pattern
## Aka, it finds an exact match 

if re.search("^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

