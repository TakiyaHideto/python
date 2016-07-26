

class JoinFoodTag:
    def __init__(self, input_file1, input_file2, output_file):
        self.input_file1 = input_file1
        self.input_file2 = input_file2
        self.output_file = output_file
        self.food_tag_dict1 = {}
        self.food_tag_dict2 = {}

    def loadData(self, input_file, dict):
        with open(input_file, "r") as file_in:
            for line in file_in:
                elements = line.rstrip().split("\t")
                dict[elements[0]] = elements[1]
        return dict

    def writeFile(self, output_file, dict1, dict2):
        with open(output_file, "w") as file_out:
            for key in dict1:
                if int(dict1[key])<5000:
                    continue
                if key in dict2:
                    file_out.write("{0}\t{1}\n".format(key, dict2[key]))
                else:
                    file_out.write("{0}\t{1}\n".format(key, "unknown"))

    def runMe(self):
        food_set_dict = self.loadData(self.input_file1, self.food_tag_dict1)
        food_attr_dict = self.loadData(self.input_file2, self.food_tag_dict2)
        self.writeFile(self.output_file, food_set_dict, food_attr_dict)

if __name__ == "__main__":
    input_file1 = '/Users/hideto/Desktop/temp_result2'
    input_file2 = '/Users/hideto/Desktop/food_attr.txt'
    output_file = '/Users/hideto/Desktop/food_tag.txt'
    job = JoinFoodTag(input_file1, input_file2, output_file)
    job.runMe()