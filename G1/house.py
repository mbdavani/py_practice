name = input("What's your name? ")

def main(x):
    if name == "Harry" or name == "Hermione" or name == "Ron":
        print("Gryffindor")
    elif name == "Draco":
        print("Slytherin")
    else:
        print("Who?")

## This will call and use the function. It is hidden in order to show the V2 version

#main(name)


## This code will ignore anything that isn't explicitly specified normally
def main2(x):
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _                  # This will respond to anything we haven't specified
            print("Who?")


main2(name)