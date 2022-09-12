## Version 4 of the data. Tighten the code up

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")

        student = {"name": name, "house": house}
        students.append(student)


## Instead of passing a function to key, I can pass a LAMBDA function. this is a function that has no definition
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
