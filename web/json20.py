import json

with open('messages.json') as json_file:
    data = json.loads(json_file)
    for p in data:
        print (p)
