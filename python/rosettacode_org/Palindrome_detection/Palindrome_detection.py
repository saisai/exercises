pal_string = "In girum imus nocte et consumimur igni"
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("abccba"))


def is_palindrome_2(s):
    low = 0
    high = len(s) - 1
    print(high)
    while low < high:
        print(low)
        print(s[low])
        if not s[low].isalpha():
            low += 1
        elif not s[high].isalpha():
            high -= 1
        else:
            if s[low].lower() != s[high].lower():
                return False
            else:
                low += 1
                high -= 1
                return True

print(is_palindrome_2("Go"))

def is_palindrome_r(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome_r(s[1:-1])

print(is_palindrome_r("aa"))

def is_palindrome_r2(s):
  return not s or s[0] == s[-1] and is_palindrome_r2(s[1:-1])

print(is_palindrome_2("aa"))


def test(f, good, bad):
    assert all(f(x) for x in good)
    assert not any(f(x) for x in bad)
    print(
    '%s passed all %d tests' % (f.__name__, len(good) + len(bad))
    )

pals = ('', 'a', 'aa', 'aba', 'abba')
notpals = ('aA', 'abA', 'abxBa', 'abxxBa')
for ispal in is_palindrome, is_palindrome_r, is_palindrome_r2:
    test(ispal, pals, notpals)

def p_loop():
  import re, string
  re1=""       # Beginning of Regex
  re2=""       # End of Regex
  pal=input("Please Enter a word or phrase: ")
  pd = pal.replace(' ','')
  for c in string.punctuation:
     pd = pd.replace(c,"")
  if pal == "" :
    return -1
  c=len(pd)   # Count of chars.
  loops = (c+1)//2
  for x in range(loops):
    re1 = re1 + "(\w)"
    if (c%2 == 1 and x == 0):
       continue
    p = loops - x
    re2 = re2 + "\\" + str(p)
  regex= re1+re2+"$"   # regex is like "(\w)(\w)(\w)\2\1$"
  #print(regex)  # To test regex before re.search
  m = re.search(r'^'+regex,pd,re.IGNORECASE)
  if (m):
     print("\n   "+'"'+pal+'"')
     print("   is a Palindrome\n")
     return 1
  else:
     print("Nope!")
     return 0

p_loop()