"""
You are given an integer n.
Each number from 1 to n is grouped according to the sum of its digits.
Return the number of groups that have the largest size.

Example 1:
    Input: n = 13
    Output: 4
    Explanation: There are 9 groups in total, they are grouped according sum of its digits
        of numbers from 1 to 13:
            [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
            There are 4 groups with largest size.

Example 2:
    Input: n = 2
    Output: 2
    Explanation: There are 2 groups [1], [2] of size 1.

Constraints:
    1 <= n <= 10**4

A:
    n = 0   ->  not possible
    
D:
    counts = Counter()
    for i in range(1,n+1):
        digs = []
        while i:
            digs.append(i%10)
            i //= 10
        counts.update(sum(digs))
    max_count = counts(max(counts))
    return sum(1 for k in counts if counts[k] == max_count)
"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import Counter

        counts = Counter()
        for i in range(1, n + 1):
            digs = []
            while i:
                digs.append(i % 10)
                i //= 10
            counts.update([sum(digs)])
        max_count = counts[max(counts, key=lambda x: counts[x])]
        return sum(1 for k in counts if counts[k] == max_count)


cases = [(13, 4), (2, 2)]

sol = Solution()
for (n, exp) in cases:
    assert (
        got := sol.countLargestGroup(n)
    ) == exp, f"Failed case ({n}) - expecting ({exp}), got ({got})"
