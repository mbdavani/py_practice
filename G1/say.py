import cowsay
import sys

if len(sys.argv) == 2:
    # COWSAY is not like PRINT. You can not pass in multiple arguments with a COMMA
    # you must concatenate using a PLUS symbol
    #cowsay.cow("Hello, " + sys.argv[1])
    cowsay.trex("Hello, " + sys.argv[1])


