## The older version of hte code
#with open("students.csv") as file:
#    for line in file:
#        row = line.rstrip().split(",")
#        print(f"{row[0]} is in {row[1]}")

with open("students.csv") as file:
    for line in file:
        ## When you have a variable that is a list, you dont have to throw all of that list into a variable
        ## This will split the line, and create two variables at once
        ## This will "Unpack" the data simultaneously, into two variables
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")