# s = "longest-substring-without-repeating-characters"
# print(s.title().replace('-', ''))

import sys

def getTitle(title):
    return title.title().replace('-', '')

def getTitle2(title):
    return title.title()



if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Enter correct argument")

    print(getTitle(sys.argv[1]))
    print(getTitle2(sys.argv[1]))
