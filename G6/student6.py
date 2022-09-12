## Classes
## Classes allow us to create custom containers with custom names for pieces of data


# In classes, there are not only attributes/instance variables you can put inside of them, but also methods
# Classes come with certain methods (functions) that you can define within them, and they behave a special way
## A METHOD IS A FUNCTION INSIDE OF A CLASS

class Student:
    def __init__(self, name, house):  # We add instance variables to the STUDENT object
        self.name = name
        self.house = house



def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    # with classes, unlike dictionaries, we can standardize attributes and what kind of values you can set them to
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)      # Just by defining a Class, you get a function identical to the name of that class
    # We treat the name of the class as a function here
    # We pass in two values, "Name and house". This is known as a Constructor Call
    # this above line of code will construct a "Student" object for us, using synonyms it will instantiate a "Student" object.
    # To create the object, it will use the "Student" class as a template.

    return student


if __name__ == "__main__":
    main()
