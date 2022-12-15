"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        from math import factorial

        def choose(n, k):
            return factorial(n) // (factorial(n - k) * factorial(k))

        ways = 1
        one_cnt = n
        two_cnt = 0
        while one_cnt > 1:
            one_cnt -= 2
            two_cnt += 1
            ways += choose(two_cnt + one_cnt, two_cnt)

        return ways


sol = Solution()
for i in range(10):
    print(f"Stair count = {i}. Ways: {sol.climbStairs(i)}")
