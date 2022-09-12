def main():
    x = get_integer()
    print(f"x is {x}")

def get_integer():
    while True:
        try:
            x = int(input("What's X? "))
        except ValueError:
            print("X is not an integer")
            # if X is not an integer, BREAK will immediately end the LOOP, and then re-run the code
        else:
            # The ELSE code is associated with the TRY code here.
            # if nothing goes wrong, ELSE tells the code to do the following:
            break
    return x    
    # you can delete RETURN in line 17, and replace BREAK in line 16 with it
    # RETURN does the same thing as BREAK, but better.    
    



# Below is a more neatly organized version of Lines 1-20:
def main2():
    x = get_integer2("What's X? ")
    print(f"x is {x}")    

# This is an upgraded version of get_integer
# This code uses "prompt" to be more generically asking a user for *a* integer, as defined by the coder
def get_integer2(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass

# main()
main2()