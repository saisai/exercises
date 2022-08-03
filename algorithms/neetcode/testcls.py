

class S:

    def __init__(self):
        self.test = {}

    @classmethod
    def test(cls, nums):
        i = 1
        for a in ['a', 'b', 'c']:
            cls[a] = i
            i += 1

        return cls

print(S.test(10))

