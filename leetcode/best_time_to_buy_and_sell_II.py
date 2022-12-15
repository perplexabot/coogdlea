"""Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you
like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must
sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        nsf = max(prices) + 1
        xsf = -1
        total = 0

        for i in prices:
            if i <= nsf:
                if xsf != -1:
                    total += xsf - nsf
                nsf = i
                xsf = -1
            elif i > nsf and i < xsf:
                total += xsf - nsf
                nsf = i
                xsf = -1
            else:
                xsf = max(i, xsf)

        if xsf != -1:
            total += xsf - nsf

        return total


inps = [
    ([7, 1, 5, 3, 6, 4], 7),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2, 3, 4, 5], 4),
    ([], 0),
    ([1], 0),
    ([1, 2], 1),
    ([2, 1], 0),
    ([7, 1, 10, 2, 5, 4], 12),
    ([1, 5, 10, 22], 21),
    ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 15),
]

sol = Solution()
for p, exp in inps:
    print(f'Finding max profit for {p} and asserting...')
    assert exp == sol.maxProfit(p)
