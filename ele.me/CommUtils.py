# common utilities

def sort(array):
    return sort(array)

def stringToInt(arrayString):
    try:
        return map(lambda x:int(x), arrayString)
    except Exception:
        print "Wrong Type var in array"

def intToString(arrayInt):
    try:
        return map(lambda x:str(x), arrayInt)
    except Exception:
        print "Wrong Type var in array"

def extractColumnFromString(array, separater, index):
    try:
        return map(lambda x:x.split(separater)[index], array)
    except Exception:
        print "Exception"