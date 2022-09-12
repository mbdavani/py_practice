## This tests the RE library
## This library provides the ability to define, check for, and replace patterns.
## https://docs.python.org/3/library/re.html

## Previous code was too tolerant, we need to have some requirements for the username
import re

email = input("What's your email address? ").strip()#.lower()

## a-z means a through z
## Do not type in spaces between the things you care about
#if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):

## This can be streamlined with the following patterns:
## \d  decimal digit
## \D not a decimal digit
## \s whitespace characters
## \S not a whitespace character
## \w word character...as well as numbers and underscores\
## \W not a word character


#if re.search("^\w+@\w+\.edu$", email.lower()):

## (\w+\.)? was added to take into account emails like sam@cs50.harvard.edu
if re.search("^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
