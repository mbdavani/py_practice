## Prompt users the URL, and extract the user's username
import re

url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")



## "?" means 0 or more of the item immediately before it are allowed
## We allow "HTTP" or "HTTPS"
## We allow a www. or none at all
## We all a protocol (HTTPS|HTTP) or non at all. This means just "twitter.com/"" works

username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)

print(f"Username: {username}")

