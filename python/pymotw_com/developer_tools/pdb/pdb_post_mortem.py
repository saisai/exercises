class MyObj:

    def __init__(self, num_loops):
        self.count = num_loops

    def go(self):
        for i in range(self.num_loops):
            print(i)
        return