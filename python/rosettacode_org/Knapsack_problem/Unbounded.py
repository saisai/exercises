class Bounty:
    def __init__(self, value, weight, volume):
        self.value, self.weight, self.volume = value, weight, volume
 
panacea = Bounty(3000,  0.3, 0.025)
ichor =   Bounty(1800,  0.2, 0.015)
gold =    Bounty(2500,  2.0, 0.002)
sack =    Bounty(   0, 25.0, 0.25)
best =    Bounty(   0,    0, 0) 
current = Bounty(   0,    0, 0) 
 
best_amounts = (0, 0, 0)
 
max_panacea = int(min(sack.weight // panacea.weight, sack.volume // panacea.volume))
max_ichor   = int(min(sack.weight // ichor.weight,   sack.volume // ichor.volume))
max_gold    = int(min(sack.weight // gold.weight,    sack.volume // gold.volume))

for npanacea in range(max_panacea):
    for nichor in range(max_ichor):
        for ngold in range(max_gold):
            current.value = npanacea * panacea.value + nichor * ichor.value + ngold * gold.value
            current.weight = npanacea * panacea.weight + nichor * ichor.weight + ngold * gold.weight
            current.volume = npanacea * panacea.volume + nichor * ichor.volume + ngold * gold.volume

            if current.value > best.value and current.weight <= sack.weight and \
               current.volume <= sack.volume:
                best = Bounty(current.value, current.weight, current.volume)
                best_amounts = (npanacea, nichor, ngold)


print("Maximum value achievable is", best.value)
print("This is achieved by carrying (one solution) %d panacea, %d ichor and %d gold" % \
       (best_amounts[0], best_amounts[1], best_amounts[2]))
print("The weight to carry is %4.1f and the volume used is %5.3f" % (best.weight, best.volume))
