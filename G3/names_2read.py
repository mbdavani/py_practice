##This will load and read the file

with open("names.txt", "r") as file:
    ## File IO documentation
    ## this will read all the lines in the file, and store them in a variable
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())
    #print("Hello,", line, end="")