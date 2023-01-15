import random

outcomes = {
    'heads': 0,
    'tails': 0,
}
sides = list(outcomes.keys())
print(sides)
for i in range(10000):
    outcomes[random.choice(sides)] += 1

print(outcomes)
print('Heads:', outcomes['heads'])
print('Tails:', outcomes['tails'])