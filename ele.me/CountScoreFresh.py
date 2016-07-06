import json
import ParseJson as pj
import CommUtils as cu

class CountScoreFresh:
    def __init__(self, inputFile):
        self.inputFile = inputFile
        self.scoreFreshDict = {}
        self.scoreMax = 0.0
        self.scoreMin = 0.0

    def __loadData(self):
        with open(self.inputFile, "r") as fileIn:
            for line in fileIn:
                if line.startswith("{") is False:
                    continue
                jsonObject = pj.parseJson(line)
                for key in jsonObject.keys():
                    foodName = key
                    preferScore = round(jsonObject[foodName]["score"],1)
                    isFresh = jsonObject[foodName]["is_fresh"]
                    self.__putInfoIntoDict(self.scoreFreshDict, key="{0}_{1}".format(preferScore, isFresh))
                    self.scoreMax = max(self.scoreMax, preferScore)
                    self.scoreMin = min(self.scoreMin, preferScore)

    def __putInfoIntoDict(self, dict, key):
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1

    def __pritnInfo(self):
        print "max:{0}".format(self.scoreMax)
        print "min:{0}".format(self.scoreMin)

    def __sortScoreFreshDict(self):
        tmpList = cu.extractColumnFromString(self.scoreFreshDict, separater="_", index=0)
        tmpList = cu.stringToInt(tmpList)
        tmpList = sorted(tmpList)
        tmpList = cu.intToString(tmpList)
        for key in tmpList.keys():
            print "{0}_{1}:{2}".format(key, "0", self.scoreFreshDict[key+"0"])
            print "{0}_{1}:{2}".format(key, "1", self.scoreFreshDict[key + "1"])


    def runMe(self):
        self.__loadData()
        self.__sortScoreFreshDict()
        self.__pritnInfo()

if __name__ == "__main__":
    inputFile = "/home/jiahao.dong/test_file"
    job = CountScoreFresh(inputFile)
    job.runMe()