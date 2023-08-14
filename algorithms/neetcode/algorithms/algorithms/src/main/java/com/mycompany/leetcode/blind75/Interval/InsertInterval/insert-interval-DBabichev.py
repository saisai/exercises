
class S:
    def insert(self, intervals, I):
        res, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < I[0]:
                res.append([x, y])
            elif I[1] < x:
                i -= 1
            else:
                I[0] = min(I[0], x)
                I[1] = min(I[1], y)

        return res + [I] + intervals[i+1:]



intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(S().insert(intervals, newInterval))
