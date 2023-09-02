
class S:
    def eraseOverlapIntervals(self, intervals):
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt
    
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(S().eraseOverlapIntervals(intervals))