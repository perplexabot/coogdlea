"""Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up
to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use
the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect

        need = set()
        for ind, n in enumerate(numbers):
            if n in need:
                return [bisect.bisect_left(numbers, target - n) + 1, ind + 1]
            else:
                need.add(target - n)


inps = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([1, 3, 5, 6], 7, [1, 4]),
    ([0, 1, 2, 3, 10, 20, 21, 22], 10, [1, 5]),
    ([0, 10], 10, [1, 2]),
    ([1, 10, 11, 20, 21, 30, 31, 40], 31, [3, 4]),
    ([-5, 5], 0, [1, 2]),
    ([1, 1, 3, 3, 6, 7], 6, [3, 4]),
    ([0, 0, 3, 4], 0, [1, 2]),
]

sol = Solution()
for nums, tgt, exp in inps:
    print(f"Finding two_sum in {nums} for tgt {tgt} and asserting...")
    ans = sol.twoSum(nums, tgt)
    assert ans[0] in exp and ans[1] in exp and exp[0] in ans and exp[1] in ans
