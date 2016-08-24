#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

frq_dict = {}

# def getSortedTimestamp(time_arr):
#     time_arr_int = map(lambda x: int(x), time_arr)
#     return sorted(time_arr_int)
#
# def getTimeGapArr(time_arr):
#     time_gap_arr = []
#     for i in range(0,len(time_arr)-1):
#         time_gap_arr.append((time_arr[i+1] - time_arr[i])/(60*60*24))
#     return time_gap_arr

input_file = '/Users/hideto/Desktop/temp_result2'
with open(input_file, 'r') as file_in:
    for line in file_in:
        if '套餐' in line:
            continue
        elements = line.rstrip().split('\t')
        time_arr = elements[2].replace('[','').replace(']','').split(',')
        if str(len(time_arr)) in frq_dict.keys():
            frq_dict[str(len(time_arr))] += 1
        else:
            frq_dict[str(len(time_arr))] = 1

print 'finish load data into dict'

dict_keys = sorted(map(lambda x:int(x), frq_dict.keys()))

for key in dict_keys:
    print '{0}\t{1}'.format(key, frq_dict[str(key)])

