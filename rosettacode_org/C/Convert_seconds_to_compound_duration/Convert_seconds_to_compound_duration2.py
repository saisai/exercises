

def duration(seconds, _maxweeks=99999999999):
    return ', '.join('%d %s' % (num, unit)
            for num, unit in zip([(seconds // d) % m
                for d, m in ((604800, _maxweeks),
                    (86400, 7), (3600, 24),
                    (60, 60), (1, 60))],
                ['wk', 'd', 'hr', 'min', 'sec'])
            if num)

for seconds in [7259, 86400, 6000000]:
    print("%7d sec = %s" % (seconds, duration(seconds)))

