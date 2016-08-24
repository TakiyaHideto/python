#coding=utf-8

import re

class PredictSexWithBayes:
    def __init__(self, input_file):
        self.input_file = input_file
        self.char_freq_dict = {}
        self.char_male_freq_dict = {}
        self.char_female_freq_dict = {}
        self.sex_freq_dict = {}
        self.sex_word_dict = locals()
        self.undined_user_list = []

    def inputDict(self, key, dict):
        if key in dict.keys():
            dict[key] += 1
        else:
            dict[key] = 1

    def inputNameInfo(self, name, dict):
        if self.isChinese(name) is True:
            for character in name.decode('utf-8'):
                self.inputDict(character.encode('utf-8'), dict)
        else:
            self.inputDict(name, dict)

    def inputSexInfoGiveName(self, sex, name, dict):
        if self.isChinese(name) is True:
            for character in name.decode('utf-8'):
                try:
                    self.inputDict(sex, dict[character])
                except KeyError:
                    dict[character] = {'1':0, '2':0}
                    self.inputDict(sex, dict[character])
        else:
            try:
                self.inputDict(sex, dict[name])
            except KeyError:
                dict[name] = {'1':0, '2':0}
                self.inputDict(sex, dict[name])

    def isChinese(self, contents):
        for ch in list(contents.decode('utf-8')):
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    def loadData(self, input_file):
        count = 0
        # with open(input_file, 'rb') as file_in:
        file_in = open(input_file, 'rb').readlines()
        for line in file_in:
            count += 1
            if count % 10000 == 0:
                print count
            try:
                elements = line.strip().split('\t')
                name = elements[0]
                sex = elements[1]
                if sex == '0':
                    self.undined_user_list.append(name)
                    continue
                # prob of single word
                self.inputNameInfo(name, self.char_freq_dict)
                # prob of single sex
                self.inputDict(sex, self.sex_freq_dict)
                # prob of word given sex
                word_prob_given_sex = {
                    '1': lambda: self.inputNameInfo(name, self.char_male_freq_dict),
                    '2': lambda: self.inputNameInfo(name, self.char_female_freq_dict)
                }
                word_prob_given_sex[sex]()
                # prob of sex given word
                self.inputSexInfoGiveName(sex, name, self.sex_word_dict)
            except IndexError:
                continue

    def sumDictValue(self, dict):
        sum = 0
        for key in dict.keys():
            sum += dict[key]
        return sum

    def predictSex(self, name):
        prob_name = 1.0
        for ch in name.decode('utf-8'):
            try:
                prob_name *= (float(self.char_freq_dict[ch.encode('utf-8')]) + 1.0) / \
                             float(self.sumDictValue(self.char_freq_dict))
            except KeyError:
                prob_name *= (1.0) / float(self.sumDictValue(self.char_freq_dict))
        prob_sex_male = float(self.sex_freq_dict['1']) / (float(self.sex_freq_dict['1']) + float(self.sex_freq_dict['2']))
        prob_sex_female = float(self.sex_freq_dict['2']) / (float(self.sex_freq_dict['1']) + float(self.sex_freq_dict['2']))
        prob_name_given_sex_male = 1.0
        prob_name_given_sex_female = 1.0
        for ch in name.decode('utf-8'):
            try:
                prob_name_given_sex_male *= (float(self.char_male_freq_dict[ch.encode('utf-8')]) + 1.0) / \
                                        float(self.sumDictValue(self.char_male_freq_dict))
            except KeyError:
                prob_name_given_sex_male *= (1.0) / float(self.sumDictValue(self.char_male_freq_dict))
            try:
                prob_name_given_sex_female *= (float(self.char_female_freq_dict[ch.encode('utf-8')]) + 1.0) / \
                                        float(self.sumDictValue(self.char_female_freq_dict))
            except KeyError:
                prob_name_given_sex_female *= (1.0) / float(self.sumDictValue(self.char_female_freq_dict))
        print name, prob_name_given_sex_male*prob_sex_male/prob_name, prob_name_given_sex_female*prob_sex_female/prob_name

    def runMe(self):
        self.loadData(self.input_file)
        for name in self.undined_user_list:
            self.predictSex(name)

if __name__ == "__main__":
    input_file = '/Users/hideto/Desktop/temp_result1'
    job = PredictSexWithBayes(input_file)
    job.runMe()












