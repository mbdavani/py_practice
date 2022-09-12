## This code validates if a user's email address works or not

email = input("What's your email address? ").strip()

if "@" in email and ".com" in email:
    print("Valid")
else:
    print("Invalid")
