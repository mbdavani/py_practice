students = [
    {"name": "Hermione", "House": "Gryffindor", "patronus" : "otter"},
    {"name": "Harry", "House": "Gryffindor", "patronus" : "Stag"},
    {"name": "Ron", "House": "Gryffindor", "patronus" : "Jack Russel Terrier"},
    {"name": "Draco", "House": "Slytherin", "patronus": None}
    # NONE is a Python keyword, which represents the absence of a value. Not necessary, but good for clarity to code reader
]

for student in students:
    print(student["name"], student["House"], student["patronus"], sep = ", ")