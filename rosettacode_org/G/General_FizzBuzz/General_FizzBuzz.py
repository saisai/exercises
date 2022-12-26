
def genfizzbuzz(factorwords, numbers):
    factorwords.sort(key=lambda p: p[0])
    lines = []
    for num in numbers:
        words = ''.join(wrd for fact, wrd in factorwords if ( num % fact ) == 0)
        lines.append(words if words else str(num))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(genfizzbuzz([(5, 'Buzz'), (3, 'Fizz'), (4, 'Baxx')], range(1, 21)))
