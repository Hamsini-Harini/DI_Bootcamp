import json

file_location = "c:/Users/Win/Desktop/Dev Institute/Week2/Day3/func.py"

with open (file_location) as file:
    contents = json.loads(file.read())
    print(contents)
