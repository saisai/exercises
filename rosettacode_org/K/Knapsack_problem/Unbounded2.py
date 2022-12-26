from collections import namedtuple
from itertools import product

Bounty = namedtuple("Bounty", "name value weight volume")

sack = Bounty("sack", 0, 25.0,0.25)
items = [Bounty('panacea', 3000,  0.3, 0.025),
         Bounty('ichor',   1800,  0.2, 0.015),
         Bounty('gold',    2500,  2.0, 0.002)]

def tot_value(items_count):
    """
    Given the count of each item in the sack return -1 if they can't be carried or their total value.

    (also return the negative of the weight and the volume so taking the max of a series of return
    values will minimise the weight if values tie, and minimise the volume if values and weights tie).
    """

    global items, sack
    weight = sum(n * item.weight for n, item in zip(items_count, items))
    volume = sum(n * item.volume for n, item in zip(items_count, items))
    if weight <= sack.weight and volume <= sack.volume:
        return sum(n * item.value for n, item in zip(items_count, items)), -weight, -volume    
    else:
        return -1, 0, 0


def knapsack():
    global items, sack
    # find max of any one item
    max1 = [min(int(sack.weight // item.weight), int(sack.volume // item.volume)) for item in items]

    # Try all combinations of bounty items from 0 up to max1
    return max(product(*[range(n + 1) for n in max1]), key=tot_value)

max_items = knapsack()
maxvalue, max_weight, max_volume = tot_value(max_items)
max_weight = -max_weight
max_volume = -max_volume


print ("The maximum value achievable (by exhaustive search) is %g." % maxvalue)
item_names = ", ".join(item.name for item in items)
print ("  The number of %s items to achieve this is: %s, respectively." % (item_names, max_items))
print ("  The weight to carry is %.3g, and the volume used is %.3g." % (max_weight, max_volume))

