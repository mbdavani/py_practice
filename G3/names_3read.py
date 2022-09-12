## Better version of names_2read.py

with open("names.txt", "r") as file:
    for line in file:
        print("hello," line.rstrip())