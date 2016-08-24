input_file = '/Users/hideto/Desktop/1.txt'

tag_set = set()

with open(input_file, 'r') as file_in:
    for line in file_in:
        elements = line.rstrip().split('#')
        for ele in elements:
            if ele not in tag_set:
                tag_set.add(ele)
    for tag in tag_set:
        print tag


print len(tag_set)