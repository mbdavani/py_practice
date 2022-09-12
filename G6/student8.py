## Further usage of Classes

class Student:
    def __init__(self, name, house, patronus): 
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):                  ## The String definition of this object
        return f"{self.name} from {self.house}"

    def charm(self):                    ## Methods/Class-functions must always have at least one argument, self, which gives access to the current object
        if self.patronus == "Stag":     ##Emojis are copy-pasted from emojipedia.com
            return "🐎"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus == "Jack Russell Terrier":
            return "🐕"
        else:
            return "Nothing Happened..."



def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)  


if __name__ == "__main__":
    main()
