from scipy import stats
import numpy as np
import pylab as pl
import CommUtils as cu
import matplotlib.pyplot as plt

def lambdaFunc(arr):
    try:
        return map(lambda x:x+30, arr)
    except Exception:
        print "Wrong Type var in array"

score_arr = []

input_file = '/Users/hideto/Desktop/temp_result1'

with open(input_file, 'r') as file_in:
    for line in file_in:
        elements = line.rstrip()
        score_arr.append(float(elements))

score_arr = sorted(score_arr)
score_arr = lambdaFunc(score_arr)
score_sum = sum(score_arr)
print score_sum

score_dict = {}
for score in score_arr:
    if str(int(score)) in score_dict:
        score_dict[str(int(score))] += 1
    else:
        score_dict[str(int(score))] = 1

key_arr = cu.numToString(sorted(cu.stringToInt(score_dict.keys())))
value_arr = []
temp_sum = 0.0
for key in key_arr:
    temp_sum += (score_dict[key]*float(key))
    value_arr.append(temp_sum/score_sum)
    print key,temp_sum/score_sum

plt.plot(key_arr, value_arr)
plt.show()