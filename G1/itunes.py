## API : Application Programming Interface
## https://itunes.apple.com/search?entity=song&limit=1&term=weezer

import json
import requests
import sys

if len(sys.argv) !=2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
## This will get a JSON file of the data from Apple's API 
#print(json.dumps(response.json(), indent=2))

## Grabs the JSON file from the URL above
VARIABLENAME = response.json()
## By running only the above code, we know that there is an object that has a KEY named "results"
## We know that this KEY, "results" is a list. This list contains 50 songs (see API URL limit=50 command)
for i in VARIABLENAME["results"]:
    print(i["trackName"])