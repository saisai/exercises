import random; print((lambda attr: f"Attributes: {attr}\nTotal: {sum(attr)}")((lambda func, roll_func: func(func, roll_func, roll_func()))((lambda func, roll_func, rolls: rolls if sum(rolls) >= 75 and rolls.count(15) >= 2 else func(func, roll_func, roll_func())), lambda: [sum(sorted(random.randint(1, 6) for _ in range(4))[1:]) for _ in range(6)])))

