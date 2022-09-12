## Version 3 of the data. This will sort the data/list by the names, not the entire sentence.
## Ver. 2 sorted the entire sentences, which is a bit silly. Let us now sort by the actual name first.

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        ## Create a dictionary.
        #student = {}
        #student["name"] = name
        #student["house"] = house
        student = {"name": name, "house": house}
        ## Now, we append this info to the "students" LIST, which was previously empty.
        ## Because this is a FOR loop, each student+their info will be uploaded, 1 by 1.
        students.append(student)


def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

## REMEMBER!! = Dictionaries use indexes based on strings
## Lists use indices based on numbers, 0,1,2, etc
for student in sorted(students, key=get_name, reverse = True):
    print(f"{student['name']} is in {student['house']}")


## visual explanation for what we did
#print(students)