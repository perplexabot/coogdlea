"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
    Input: n = 5
    Output: [-7,-1,1,3,4]
    Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
    Input: n = 3
    Output: [-1,0,1]

Example 3:
    Input: n = 1
    Output: [0]

Constraints:
    1 <= n <= 1000

A:
    n is 0 -> not possible
    n is 1 -> return 0

D:
    if n is odd:
        nums = {0}
        nums.add(range((n-1)/2)
        nums.add(-*range(n-1)/2)

    if n is even:
        m = n + 1
        nums = {0}
        nums.add(range((n-1)/2)
        nums.add(-*range(n-1)/2)
        nums[-2] += nums[-1]
        del nums[-1]

    return nums
"""

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        if not n % 2:
            m = n + 1
            positives = list(range(1, (m - 1) // 2 + 1))
            negatives = list(range(-1, -((m - 1) // 2 + 1), -1))
            nums.extend(negatives)
            nums.append(0)
            nums.extend(positives)
            nums[-2] += nums[-1]
            nums.pop()
        else:
            positives = list(range(1, (n - 1) // 2 + 1))
            negatives = list(range(-1, -((n - 1) // 2 + 1), -1))
            nums.extend(negatives)
            nums.append(0)
            nums.extend(positives)
        return nums


cases = [(5, [-2, -1, 0, 1, 2]), (3, [-1, 0, 1]), (1, [0]), (2, [-1, 1])]

sol = Solution()
for (case, exp) in cases:
    assert (got := set(sol.sumZero(case))) == set(
        exp
    ), f"Failed case ({case}) - expecting ({exp}), got ({got})."
