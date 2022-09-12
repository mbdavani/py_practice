## Version 6. We now have assigned a Title row for the columns in the new CSV file. We no longer need csv.reader


import csv

students = []

with open("students_6.csv") as file:
    ## DictReader will iterate over the file, from top to bottom, loading each line of text as a dictionary of columns, not a list of columns
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
## With our Columns clearly titled or named, no matter what order the columns are sorted by, 
## we will always pull the right data/column


## Instead of passing a function to key, I can pass a LAMBDA function. this is a function that has no definition
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
