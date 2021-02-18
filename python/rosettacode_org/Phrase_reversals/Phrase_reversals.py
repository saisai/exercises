phrase = "rosetta code phrase reversal"
print(phrase)

print(phrase[::-1]) # Reversed

t = ' '.join(word[::-1] for word in phrase.split())  # Words reversed.
print(t)

t = ' '.join(phrase.split()[::-1])      # Word order reversed
print(t)
