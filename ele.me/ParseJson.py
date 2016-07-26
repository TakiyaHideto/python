# this python script is for parsing string to json

import json

def parseJson(jsonString):
    jsonObject = json.loads(jsonString)
    return jsonObject

def extractValue(jsonObject, key):
    # the parameter key is required as string
    return jsonObject[key]
