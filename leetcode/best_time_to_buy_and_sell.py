"""Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one
share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

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
        sums = set([0])

        for i in prices:
            if i < nsf:
                sums.add(xsf - nsf)
                nsf = i
                xsf = -1
            else:
                xsf = max(i, xsf)

        sums.add(xsf - nsf)
        return max(sums)


inps = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([7, 1, 10, 2, 5, 4], 9),
    ([7, 1, 10, 2, 20, 5], 19),
    ([7, 2, 20, 1, 10, 5], 18),
    ([1, 2, 3, 4], 3),
    ([], 0),
    ([1], 0),
]

sol = Solution()
for ind, (p, expected) in enumerate(inps):
    print(f"Finding max profit for {p} and asserting...")
    print(f" GOT: {sol.maxProfit(p)}")
    assert expected == sol.maxProfit(p)
