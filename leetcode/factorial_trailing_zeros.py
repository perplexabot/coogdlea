"""Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
"""


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr = 2
        i = 1
        tot = 0
        while curr > 1:
            curr = n // (5 ** i)
            tot += curr
            i += 1
        return tot


from math import factorial
from itertools import groupby

sol = Solution()
for i in range(4000):
    print(f"Finding trailing zeros for {i}! and asserting...")
    ans = sol.trailingZeroes(i)
    g = groupby(str(factorial(i)))
    l = [(x, list(y)) for x, y in g]
    exp = len(l[-1][1]) if '0' == l[-1][0] else 0
    assert ans == exp

