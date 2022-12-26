from itertools import product

while True:
    bexp = input('\nBoolean expresson: ')
    bexp = bexp.strip()
    if not bexp:
        print("\nThank you")
        break
    code = compile(bexp, '<string>', 'eval')
    names = code.co_names
    print('\n' + ' '.join(names), ':', bexp)
    for values in product(range(2), repeat=len(names)):
        env = dict(zip(names, values))
        print(' '.join(str(v) for v in values), ':', eval(code, env))

# A ^ B
# A | B
# A & B
# ~A
# S | ( T ^ U )

# http://rosettacode.org/wiki/Truth_table#Python