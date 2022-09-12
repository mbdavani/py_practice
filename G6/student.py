def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}") # A Tuple is immutable, which means it can never be editted, unlike a List

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) # this is a Tuple, one variable with two things in it


if __name__ == "__main__":
    main()
