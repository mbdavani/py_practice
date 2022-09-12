## Prompt users the URL, and extract the user's username
import re

url = input("URL: ").strip()



## We use (?:www\.) to say 'Yes, I am grouping these things together, but no, you do not need to capture them (turn it into a group)

## re.Search creates a group, starding with an index of 1 (NOT 0)
### The "Groups" are what are in the parenthesis


#matches = re.search("^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
#if matches:
#    print(f"Username:", matches.group(1))

## Now, we use the walrus operator to transform lines 14-16 into:
##   We also change ".+" to allow any characters, to only alphanumeric characters and underscore
##   By doing this, we can now remove the $ from the end of the code. This is because we will only accept the username, and thus,
##       anything after the username will be ignored
if matches := re.search("^https?://(?:www\.)?twitter\.(?:com|org)/([a-z0-9_])", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
