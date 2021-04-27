import json


def load(fileName):
    file = open(f"./1/{fileName}.json", "r")
    data = json.loads(file.read())
    return(data)
    

def get_key(d, value):
    for key, val in d.items():
        if  val >= value:
            return key




