def eraseOverlapIntervals(intervals):
    current = float('-inf')
    count = 0
    sInterv = sorted(intervals, key=lambda i: i.end)
    for interval in sInterv:
        if interval.start >= current:
            current = interval.end
            count += 1
    return len(intervals) - count

class Intervals:
    def __init__(self, s=0,e=0):
        self.start = s
        self.end = e

import random
l = []
for i in range(10):
    t = Intervals(i, i + random.randint(0,10))
    l.append(t)
ans = eraseOverlapIntervals(l)
print("ans: ", ans)
