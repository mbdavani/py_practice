## Version 2 of the original file. This will sort the data
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        ## The below line will append this to our list, NOT the file
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)