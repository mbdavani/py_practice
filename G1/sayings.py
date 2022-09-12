def main():
    hello("World")
    goodbye("World")


def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    ## We use F string in Python in order to incorporate the variable directly into PRINT
    print(f"Goodbye, {name}")

## This will run the below code IF the "name" of the function is the same as the file it is in
## Specifically, this means that you can use this to test this Python LIBRARY, but if we call
## these LIBRARY functions in a different code, it won't accidentally run the entire LIBRARY, 
# which would happen if we instead only wrote "main()" at the end of our LIBRARY
if __name__ == "__main__":
    main()

## This is a little confusing, so look here,
print(__name__)
