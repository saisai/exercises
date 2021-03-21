
def happy(n):
    past = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True

results = [x for x in range(0, 500) if happy(x)][:8]
print(results)
