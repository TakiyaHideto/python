#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

gap_dict = {}

def getSortedTimestamp(time_arr):
    time_arr_int = map(lambda x: int(x), time_arr)
    return sorted(time_arr_int)

def getTimeGapArr(time_arr):
    time_gap_arr = []
    for i in range(0,len(time_arr)-1):
        time_gap_arr.append((time_arr[i+1] - time_arr[i])/(60*60*24))
    return time_gap_arr

input_file = '/Users/hideto/Desktop/temp_result2'
with open(input_file, 'r') as file_in:
    for line in file_in:
        if '套餐' in line:
            continue
        elements = line.rstrip().split('\t')
        time_arr = getSortedTimestamp(elements[2].replace('[','').replace(']','').split(','))
        time_gap_arr = getTimeGapArr(time_arr)
        for time_gap in time_gap_arr:
            if str(time_gap) in gap_dict.keys():
                gap_dict[str(time_gap)] += 1
            else:
                gap_dict[str(time_gap)] = 1

print 'finish load data into dict'

dict_keys = sorted(map(lambda x:int(x), gap_dict.keys()))

for key in dict_keys:
    print '{0}\t{1}'.format(key, gap_dict[str(key)])

