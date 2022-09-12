## This tests the RE library
## This library provides the ability to define, check for, and replace patterns.
## https://docs.python.org/3/library/re.html


## If you type in "malan@@@harvard.edu", it counts as VALID
## Therefore, this code will remedy that problem, relative to VER.#4
import re

email = input("What's your email address? ").strip()


## Inside of the Search, you can use [] to match only the symbols inside the bracket
## Inside of the Search, you can use [^] to mean you can NOT match any of these characters

# if re.search("^[abcdefgeh]+\.edu$", email):

if re.search("^[^@]+@[^@]\.edu$", email):
    print("Valid")
else:
    print("Invalid")

## You can also use:
#if re.search(".{1}.*@.*", email):
