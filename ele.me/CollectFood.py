import os

class CollectFood:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.food_set = set()

    def __loadData(self, input_file, food_set):
        with open(input_file, "r") as file_in:
            os.linesep='\r'
            for line in file_in:
                elements = line.rstrip().split("\t")
                try:
                    food_cat = elements[2]
                    food_set.add(food_cat)
                    food_cat = elements[3]
                    food_set.add(food_cat)
                    print elements
                except IndexError:
                    continue

    def __outputFile(self, output_file, food_set):
        with open(output_file, "w") as file_out:
            for food in food_set:
                file_out.write("{0}\n".format(food))

    def runMe(self):
        self.__loadData(self.input_file, self.food_set)
        self.__outputFile(self.output_file, self.food_set)

if __name__ == '__main__':
    input_file = '/Users/hideto/Desktop/temp_result1.txt'
    output_file = '/Users/hideto/Desktop/food_set'
    job = CollectFood(input_file, output_file)
    job.runMe()
