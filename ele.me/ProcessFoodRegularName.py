#coding=utf-8

print float(2600831)/20418860

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getSeparator(line):
    if '（' in line:
        return '（'
    elif '(' in line:
        return '('
    elif ' ' in line:
        return ' '
    else:
        return 'none_separator'

specific_set = ['和合谷','小杨生煎','湘瑞轩','谷田稻香','仔皇煲','蟹蟹辣','谷田稻香']

text_arr = []
with open('/Users/hideto/Desktop/temp_result3','r') as file_in:
    for line in file_in:
        try:
            sep = getSeparator(line)

            if line.startswith(' ') is True:
                text_arr.append("{0}\t{1}\t{2}\n".format(line.rstrip(), line.rstrip(), 1.0))
                continue

            if sep == 'none_separator':
                text_arr.append("{0}\t{1}\t{2}\n".format(line.rstrip(), line.rstrip(), 1.0))
                continue

            if line.startswith('(') is True:
                if ')' in line:
                    shop_name = line.rstrip().split(')')[0].replace('(','')
                    if shop_name in specific_set:
                        text_arr.append("{0}\t{1}\t{2}\n".format(line.rstrip(), shop_name, 1.0))
                    else:
                        text_arr.append("{0}\t{1}\t{2}\n".format(line.rstrip(), line.rstrip().split(')')[1], 1.0))
                elif '）' in line:
                    shop_name = line.rstrip().split(')')[0].replace('(', '')
                    if shop_name in specific_set:
                        text_arr.append("{0}\t{1}\t{2}\n".format(line.rstrip(), shop_name, 1.0))
                    text_arr.append("{0}\t{1}\t{2}\n".format(line.rstrip(), line.rstrip().split('）')[1], 1.0))
                continue

            elements = line.rstrip().split(sep)
            text_arr.append("{0}\t{1}\t{2}\n".format(line.rstrip(), elements[0], 1.0))
        except IndexError:
            print line

with open('/Users/hideto/Desktop/temp_result4', 'w') as file_out:
    for line in text_arr:
        file_out.write(line)


