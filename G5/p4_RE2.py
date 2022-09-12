# Complete the solution so that it returns
# true if the first argument(string) passed
# in ends with the 2nd argument (also a string).

#Examples:
#solution('abc', 'bc') # returns true
#solution('abc', 'd') # returns false

from hashlib import sha3_224


string="inserthere"
ending="here"

s2 = ":-)"
e2 = ":-("
import re

def solution(string, ending):
    if re.search("^.*"+ ending +"$",string):
        print("true")#remove this for actual code
        return True
    else:
        print("false")#remove this for actual code
        return False

solution(string, ending)
solution(s2,e2)

# This does not work:
#Expected solution('!@#$%^&*() :-)', ':-)') to return True: False should equal True
#Expected solution('abc\n', 'abc') to return False: True should equal False