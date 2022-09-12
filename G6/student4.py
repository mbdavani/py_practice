## Condenses version #3's code

def main():
    student = get_student()
    if student["name"] == "Padma":  # You index into lists/tuples using #'s, but you index into Dictionaries using Strings
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house":house}


if __name__ == "__main__":
    main()
