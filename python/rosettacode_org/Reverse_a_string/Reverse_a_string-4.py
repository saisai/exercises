#print(input()[::-1])

h = "hello"
print(h[::-1])

a = "hello"
print(''.join(reversed(a)))

import unicodedata


def ureverse(ustring):
    'Reverse a string including unicode combining characters'
    groupedchars = []
    uchar = list(ustring)
    while uchar:
        if unicodedata.combining(uchar[0]) != 0:
            groupedchars[-1] += uchar.pop(0)
        else:
            groupedchars.append(uchar.pop(0))
    # Grouped reversal
    groupedchars = groupedchars[::-1]

    return ''.join(groupedchars)


def say_string(s):
    return ' '.join([s, '=', ' | '.join(unicodedata.name(ch, '') for ch in s)])


def say_rev(s):
    print(f"Input:              {say_string(s)}")
    print(f"Character reversed: {say_string(s[::-1])}")
    print(f"Unicode reversed:   {say_string(ureverse(s))}")
    print(f"Unicode reverse²:   {say_string(ureverse(ureverse(s)))}")


if __name__ == '__main__':
    ucode = ''.join(chr(int(n[2:], 16)) for n in
                    'U+0041 U+030A U+0073 U+0074 U+0072 U+006F U+0308 U+006D'.split())
    say_rev(ucode)

    ucode = ''.join(chr(int(n[2:], 16)) for n in
                    'U+006B U+0301 U+0075 U+032D U+006F U+0304 U+0301 U+006E'.split())
    say_rev(ucode)

    ucode = ''.join(chr(int(n, 16))
                    for n in ['61', '73', '20dd', '64', '66', '305'])
    say_rev(ucode)