
from itertools import islice

with open('Read_a_specific_line_from_a_file2.py') as f:
    try:
        line = next(islice(f, 6, 7))
        print(line)
    except StopIteration:
        print('Not 7 lines in file')


print(open("Read_a_specific_line_from_a_file2.py").readlines()[:7][-1])
