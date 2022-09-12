## Version 5 of the data. This uses different data. We now use "Birthplace" instead of School House
## This uses a different data file. However, we have additional Commas in the .txt file, leading to problems.
## This file solves the problem of having too many commas in a CSV file

import csv

students = []

with open("students_5.csv") as file:
    reader = csv.reader(file)
    #for row in reader:
    #    students.append({"name": row[0], "home": row[1]})
    for name, home in reader:
        students.append({"name": name, "home": home})


## Instead of passing a function to key, I can pass a LAMBDA function. this is a function that has no definition
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
