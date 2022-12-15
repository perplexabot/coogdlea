"""Given a set of non-overlapping intervals, insert a new interval into the intervals
(merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def lists_to_intervals(lst):
    return [Interval(l[0], l[1]) for l in lst]


def intervals_to_lists(lst):
    return [[i.start, i.end] for i in lst]


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]

        from bisect import bisect_right, bisect_left

        lefts = [x.start for x in intervals]
        rights = [x.end for x in intervals]

        nstart_cmp_ostarts = bisect_right(lefts, newInterval.start) - 1
        nstart_cmp_oends = bisect_left(rights, newInterval.start)
        nend_cmp_ostarts = bisect_right(lefts, newInterval.end) - 1
        nend_cmp_oends = bisect_left(rights, newInterval.end)

        # new start smaller than first start
        if nstart_cmp_ostarts == -1:
            # if newInterval contains all intervals in original
            if newInterval.end >= intervals[-1].end:
                return [newInterval]

            # if newInterval is less than all itervals
            if nend_cmp_ostarts == -1:
                return [newInterval] + intervals

            # if new end is inside preexising interval
            if nend_cmp_ostarts == nend_cmp_oends:
                newInterval.end = intervals[nend_cmp_ostarts].end
                return [newInterval] + intervals[nend_cmp_ostarts + 1 :]

            # if end between two intervals
            return [newInterval] + intervals[nend_cmp_ostarts + 1 :]

        # new start greater than last end
        if nstart_cmp_oends == len(lefts):
            return intervals + [newInterval]

        # new start inside preexisting interval
        if nstart_cmp_ostarts == nstart_cmp_oends:
            # if end inside preexisting interval
            if nend_cmp_oends == nend_cmp_ostarts:
                intervals[nstart_cmp_ostarts].end = intervals[nend_cmp_oends].end
                return intervals[: nstart_cmp_ostarts + 1] + intervals[nend_cmp_oends + 1 :]

            # if end between two intervals
            intervals[nstart_cmp_ostarts].end = newInterval.end
            return intervals[: nstart_cmp_ostarts + 1] + intervals[nend_cmp_oends:]

        # new start between two intervals
        # if new interval between two intervals
        if nstart_cmp_ostarts == nend_cmp_ostarts and nstart_cmp_oends == nend_cmp_oends:
            return (
                intervals[: nstart_cmp_ostarts + 1] + [newInterval] + intervals[nstart_cmp_oends:]
            )
        # if end inside preexising interval
        if nend_cmp_ostarts == nend_cmp_oends:
            newInterval.end = intervals[nend_cmp_oends].end
            return (
                intervals[: nstart_cmp_ostarts + 1]
                + [newInterval]
                + intervals[nend_cmp_oends + 1 :]
            )

        # if end between two other intervals
        return intervals[:nstart_cmp_oends] + [newInterval] + intervals[nend_cmp_oends:]


inps = [
    (
        [
            [1, 4],
            [10, 12],
            [13, 14],
            [16, 16],
            [19, 20],
            [21, 24],
            [33, 33],
            [36, 39],
            [44, 46],
            [48, 50],
        ],
        [5, 13],
        [[1, 4], [5, 14], [16, 16], [19, 20], [21, 24], [33, 33], [36, 39], [44, 46], [48, 50]],
    ),
    ([[1, 5], [7, 8]], [4, 4], [[1, 5], [7, 8]]),
    ([[1, 5], [7, 8]], [-1, -1], [[-1, -1], [1, 5], [7, 8]]),
    ([[1, 5], [7, 8]], [9, 9], [[1, 5], [7, 8], [9, 9]]),
    ([[1, 4], [7, 10]], [-1, 5], [[-1, 5], [7, 10]]),
    ([[1, 4], [5, 10]], [-1, 6], [[-1, 10]]),
    ([[1, 4], [5, 10]], [3, 14], [[1, 14]]),
    ([[1, 5], [7, 8]], [6, 6], [[1, 5], [6, 6], [7, 8]]),
    ([[1, 4]], [3, 3], [[1, 4]]),
    ([[1, 4]], [5, 5], [[1, 4], [5, 5]]),
    ([[1, 10]], [-4, -4], [[-4, -4], [1, 10]]),
    ([[1, 5]], [5, 7], [[1, 7]]),
    ([[1, 5]], [-1, 1], [[-1, 5]]),
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ([], [1, 100], [[1, 100]]),
    ([[1, 100]], [2, 5], [[1, 100]]),
    ([[1, 100]], [0, 101], [[0, 101]]),
    ([[1, 100]], [-5, -1], [[-5, -1], [1, 100]]),
    ([[1, 100]], [-5, 50], [[-5, 100]]),
    ([[1, 100]], [50, 105], [[1, 105]]),
    ([[1, 100]], [105, 110], [[1, 100], [105, 110]]),
    ([[5, 10], [11, 15]], [4, 10], [[4, 10], [11, 15]]),
    ([[5, 10], [11, 15]], [4, 11], [[4, 15]]),
    ([[5, 10], [11, 15]], [4, 12], [[4, 15]]),
    ([[5, 10], [11, 15]], [4, 17], [[4, 17]]),
    ([[5, 10], [11, 15]], [6, 11], [[5, 15]]),
    ([[5, 10], [11, 15]], [6, 12], [[5, 15]]),
    ([[5, 10], [11, 15]], [11, 17], [[5, 10], [11, 17]]),
    ([[5, 10], [11, 15]], [0, 1], [[0, 1], [5, 10], [11, 15]]),
    ([[5, 10], [11, 15]], [16, 17], [[5, 10], [11, 15], [16, 17]]),
]
sol = Solution()
for lsts, new_lst, exp in inps:
    print(f"Doing lsts[{lsts}] and new list[{new_lst}] and asserting...")
    intervs = lists_to_intervals(lsts)
    new_inter = lists_to_intervals([new_lst])[0]
    ans = sol.insert(intervs, new_inter)
    ans_lst = intervals_to_lists(ans)
    # print(" Got: ", ans_lst)
    # print(" exp: ", exp)
    assert ans_lst == exp
print("*** PASSED! ***")
