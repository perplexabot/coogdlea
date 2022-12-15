"""Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        no_negs_nums = [x for x in nums if x > 0]
        no_negs_nums.sort()

        if not no_negs_nums:
            return 1

        if no_negs_nums[0] != 1:
            return 1

        if len(no_negs_nums) == 1:
            return 2

        i = 1
        while i < len(no_negs_nums):
            if no_negs_nums[i] - no_negs_nums[i - 1] > 1:
                return no_negs_nums[i - 1] + 1
            i += 1
        return no_negs_nums[-1] + 1


inps = [([1, 2, 0], 3), ([3, 4, -1, 1], 2), ([7, 8, 9, 11, 12], 1), ([0], 1)]
sol = Solution()

for inp, exp in inps:
    print(f"Finding first missing + for {inp} and asserting...")
    assert sol.firstMissingPositive(inp) == exp
