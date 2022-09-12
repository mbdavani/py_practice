## Because adding too many items to a list will cause us to forget which index order is which, we should instead use a Dictionary,
## A dictionary will allow us to use a key to identify different things

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student  = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
