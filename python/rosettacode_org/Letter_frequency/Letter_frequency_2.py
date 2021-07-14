import sys
import string
if hasattr(string, 'ascii_lowercase'):
    letters = string.ascii_lowercase # python 2.2 and later
else:
    letters = string.lowercase  # Earlier versions

offset = ord('a')

def countletters(file_handle):
    """Traverse a file and compute the number of occurences of each letter
        return results as a simple 26 element list of integers."""""
    results = [0] * len(letters)
    for line in file_handle:
        for char in line:
            char =char.lower()
            if char in letters:
                results[ord(char) - offset] += 1
                # Ordianl minus ordianl of 'a' of any lowercase ASCII leter -> 0..25
    return results

if __name__ == '__main__':
    sourcedata =open(sys.argv[1])
    lettercounts = countletters(sourcedata)
    for i in range(len(lettercounts)):
        print("%s=%s" % (chr(i + ord('a')), lettercounts[i]))
