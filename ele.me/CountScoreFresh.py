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
        print self.scoreFreshDict

    def runMe(self):
        self.__loadData()
        self.__pritnInfo()

if __name__ == "__main__":
    inputFile = "/home/jiahao.dong/test_file"
    job = CountScoreFresh(inputFile)
    job.runMe()