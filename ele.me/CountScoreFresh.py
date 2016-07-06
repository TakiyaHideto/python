import json
import ParseJson as pj

class CountScoreFresh:
    def __init__(self, inputFile):
        self.inputFile = inputFile

    def __loadData(self):
        with open(self.inputFile, "r") as fileIn:
            for line in fileIn:
                if line.startswith("{") is False:
                    continue
                jsonObject = pj.parseJson(line)
                for key in jsonObject.keys():
                    foodName = key
                    print foodName

    def runMe(self):
        self.__loadData()

if __name__ == "__main__":
    inputFile = "/home/jiahao.dong/test_file"
    job = CountScoreFresh(inputFile)
    job.runMe()