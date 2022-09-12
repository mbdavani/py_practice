name = input("What's your name? ")

## Let's store the data in a .txt file
## This uses OPEN command, and you can choose *how* to open it
## "w" means open the file, and make it WRITABLE
#file = open("names.txt", "w")
## However, when we use this, it will re-create the file and overwrite the info every time we run the code.

## We want to append the new data to the same file
#file = open("names.txt", "a")
#file.write(f"{name} \n")
#file.close()

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

