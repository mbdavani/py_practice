def main():
    name = input("Whats your name? ")
    print(hello(name))


## The function takes a variable named "to", for which the default value is the STRING "world"
def hello(to="world"):
    return f"hello, {to}"



if __name__ == "__main__":
    main()




## Type the following line into the command box
## pytest test
## This will run the entire TEST folder, due to the __init__.py file, which makes that folder a LIBRARY