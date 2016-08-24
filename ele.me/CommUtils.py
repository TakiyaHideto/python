# common utilities

def stringToFloat(arrayString):
    try:
        return map(lambda x:float(x), arrayString)
    except Exception:
        print "Wrong Type var in array"

def stringToInt(arrayString):
    try:
        return map(lambda x:int(x), arrayString)
    except Exception:
        print "Wrong Type var in array"

def numToString(arrayInt):
    try:
        return map(lambda x:str(x), arrayInt)
    except Exception:
        print "Wrong Type var in array"

def extractColumnFromString(array, separater, index):
    try:
        return map(lambda x:x.split(separater)[index], array)
    except Exception:
        print "Exception"