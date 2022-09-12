## Show the ratio of failure rate of a printer, which prints out a Stringcode.
## A-M are considered successful, but if it prints out something else, then its an error.
## Show answer as a fraction

import re
def printer_error(s):
    failrate=0
    failratio=0
    
    if len(s)>0: 
        for i in s:
            if re.search("[a-mA-M]", i):
                pass
            else:
                failrate += 1
        failratio=(f"{failrate}/{len(s)}")

    print(failrate)
    print(failratio)
    return failratio

s = input("What is the Output code, in letters? ")
failratio = printer_error(s)
#print(failratio)







## BETTER SOLUTION
def printer_error2(s):
    import re
    return str(len(re.findall('[n-z]', s))) + "/" + str(len(s))


## BETTER SOLUTION #2
def printer_error3(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

## BEST SOLUTION
#rom re import sub
def printer_error4(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
