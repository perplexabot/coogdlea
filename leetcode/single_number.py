"""Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:

Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        cnts = defaultdict(int)
        for e in nums:
            cnts[e] += 1
            if cnts[e] == 2:
                del cnts[e]
        return list(cnts.keys())[0]


inps = [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1), ([4, 5, 4, 6, 5, 6, 777], 777)]

sol = Solution()
for inp, exp in inps:
    print(f'Finding single in {inp} and asserting...')
    assert exp == sol.singleNumber(inp)
