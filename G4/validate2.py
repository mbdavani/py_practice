## This code validates if a user's email address works or not

email = input("What's your email address? ").strip()

username, domain = email.split("@")

## If username has 1 or more characters, it will return 1, or be "True"
## Parenthesis not needed
if (username) and ("." in domain):
    print("Valid")
else:
    print("Invalid")



