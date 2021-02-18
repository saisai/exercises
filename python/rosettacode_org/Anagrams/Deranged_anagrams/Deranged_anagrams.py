
import urllib.request
from collections import defaultdict
from itertools import combinations


def getwords(url='../unixdict.txt'):
    #return list(set(urllib.request.urlopen(url).read().decode().split()))
    return list(set(open(url).read().split()))


def find_anagrams(words):
    anagram = defaultdict(list) # map sorted chars to anagrams
    for word in words:
        anagram[tuple(sorted(word))].append(word)
    return dict((key, words) for key, words in anagram.items() if len(words) > 1 )

def is_deranged(words):
    'returns pairs of words that have no character in the same position'
    return [ (word1, word2)
            for word1, word2 in combinations(words, 2)
            if all(ch1 != ch2 for ch1, ch2 in zip(word1, word2))]

def largest_deranged_ana(anagrams):
    ordered_anagrams = sorted(anagrams.items(),
                              key=lambda x:(-len(x[0]), x[0]))
    for _, words in ordered_anagrams:
        deranged_pairs = is_deranged(words)
        if deranged_pairs:
            return deranged_pairs
    return []
    
def most_deranged_ana(anagrams):
    ordered_anagrams = sorted(anagrams.items(),
                              key=lambda x:(-len(x[0]), x[0]))
    many_anagrams = [anas for _, anas in ordered_anagrams if len(anas) > 2]
    d_of_anas = [is_deranged(ana_group) for ana_group in many_anagrams]
    d_of_anas = [d_group for d_group in d_of_anas if d_group]
    d_of_anas.sort(key=lambda d_group:(-len(d_group), -len(d_group[0])))
    mx = len(d_of_anas[0])
    most = [sorted(d_group) for d_group in d_of_anas if len(d_group) == mx]
    return most    



if __name__ == '__main__':
    #print(getwords())
    words = getwords()
    print("word count: ", len(words))

    anagrams = find_anagrams(words)
    print(anagrams)
    print("Anagram count:", len(anagrams), "\n")

    print("Longest anagrams with no characters in the same position:")
    print(' ' + '\n  '.join(', '.join(pairs)
                            for pairs in largest_deranged_ana(anagrams)))
                            
    most = most_deranged_ana(anagrams)
    print(f"\nThere are {len(most)} groups of anagrams all containing" 
          f" a max {len(most[0])} deranged word-pairs:")
    for pairs in most:
        print()
        print('  ' + '\n  '.join(', '.join(p) for p in pairs))

