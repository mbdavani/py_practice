# Demonstrates sys.argv

# Argument Variable
# creates a variable that is a list of all the words that a user has tried to input
# you can use this as feedback to improve/adjust your code
# docs.python.org/3/library/sys.html

import sys


# VERSION 1
#try:
#    print("hello, my name is", sys.argv[1])
#except IndexError:
#    print("Too few arguments")


# VERSION 2
#if len(sys.argv) <2:
#    print("Too few arguments")
#elif len(sys.argv)>2:
#    print("Too many arguments")
#else: 
#    print("Hello, me name is", sys.argv[1])



# VERSION 3
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) >2:
    sys.exit("Too many arguments")

# We take a SLICE of the list
# we take the slice, starting at 1, not 0. This continues through the end
for _ in sys.argv[1:]:
    print("hello, my name is", _)
