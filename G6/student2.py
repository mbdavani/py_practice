## Because Padma's School House is inconsistent across Book vs Movie, we will correct it manually
## We had to change the Tuple to a List in order to do so

def main():
    student = get_student() ## If the student's name is Padma, we will overwrite the value and fix it
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] ## This is a List, which supports Item Assignment

if __name__ == "__main__":
    main()
