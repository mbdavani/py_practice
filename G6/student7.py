## Further usage of Classes

class Student:
    def __init__(self, name, house):  # We add instance variables to the STUDENT object
        #if name == ""
        if not name:
            ## You could use Sys.exit("Missing Name") and import SYS
            ## However, it would be better to raise an error
            raise ValueError("Missing Name")
        
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self.name = name
        self.house = house

def __str__(self):
    return "a student"


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  


if __name__ == "__main__":
    main()
