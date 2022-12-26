with open('Read_a_specific_line_from_a_file.py') as f:
    for i, line in enumerate(f):
        print(i, line, end="")
        if i == 6:
            break
    else:
        print('Not 7 lines in file')
        line = None
