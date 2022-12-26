from collections import deque

def simplemovingaverage(period):
    assert period == int(period) and period > 0, "Period must be an interger > 0"
    summ = n = 0.0
    values = deque([0.0] * period) # old value deque

    def sma(x):
        nonlocal summ, n

        values.append(x)
        summ += x - values.popleft()
        n = min(n+1, period)
        return summ / n
    return sma

data = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

for period in data:
    print ("\nSIMPLE MOVING AVERAGE (procedural): PERIOD =", period)
    sma = simplemovingaverage(period)
    for i in range(1,6):
        print ("  Next number = %-2g, SMA = %g " % (i, sma(i)))
    for i in range(5, 0, -1):
        print ("  Next number = %-2g, SMA = %g " % (i, sma(i)))
