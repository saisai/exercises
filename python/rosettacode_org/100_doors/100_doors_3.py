
for i in range(1, 101):
    if i**0.5 % 1:
        state = 'closed'
    else:
        state = 'open'

    print("Door {}:{}".format(i, state))

i = 0
for i in range(1, 11): print("Door %s is open" % i **2)
