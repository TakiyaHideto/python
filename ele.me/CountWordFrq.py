
input_file='/Users/hideto/Desktop/word_list.txt'
output_file='/Users/hideto/Desktop/word_frq.txt'

word_frq_dict = {}

with open(input_file,'r') as file_in:
    for line in file_in:
        word = line.rstrip()
        if word in word_frq_dict:
            word_frq_dict[word] += 1
        else:
            word_frq_dict[word] = 1

with open(output_file, 'w') as file_out:
    for key in word_frq_dict.keys():
        file_out.write("{0}\t{1}\n".format(key, word_frq_dict[key]))