from collections import defaultdict
import string

if hasattr(string, 'ascii_lowercase'):
    letters = string.ascii_lowercase       # Python 2.2 and later
else:
    letters = string.lowercase             # Earlier versions


def countletters(file_handle):
    """Count occurences of letters and return a dictionary of them
        """
    results = defaultdict(int)
    for line in file_handle:
        for char in line:
            if char.lower() in letters:
                c = char.lower()
                results[c] += 1
    return results

if __name__ == '__main__':
    sourcedata = open('Letter_frequency_3.py')
    for key, val in countletters(sourcedata).items():
        print(key, '=> ', val)