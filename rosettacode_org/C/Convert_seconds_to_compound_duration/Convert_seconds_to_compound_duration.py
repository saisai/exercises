
def duration(seconds):
    t = []
    for dm in (60, 60, 24, 7):
        seconds, m = divmod(seconds, dm)
        print(seconds, m)
        t.append(m)
    t.append(seconds)
    print(t)
    return ', '.join('%d %s' % (num, unit)
            for num, unit in zip(t[::-1], 'wk d hr min sec'.split())
            if num)

for seconds in [7259, 86400, 6000000]:
    print("%7d sec = %s" % (seconds, duration(seconds)))

