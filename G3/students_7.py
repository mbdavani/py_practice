## Lecture 5/6, April 14th, CS50P Harvard
## Now we will create the CSV file on our own, from scratch
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

## Open in Append mode. It will not change the code, but will append to it.
## It will create the file if necessary, if it did not exist already
with open("students_7.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})