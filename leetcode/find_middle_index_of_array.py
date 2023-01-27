"""
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest
    amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] ==
    nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if
    middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

Example 1:
    Input: nums = [2,3,-1,8,4]
    Output: 3
    Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
    The sum of the numbers after index 3 is: 4 = 4

Example 2:
    Input: nums = [1,-1,4]
    Output: 2
    Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
    The sum of the numbers after index 2 is: 0

Example 3:
    Input: nums = [2,5]
    Output: -1
    Explanation: There is no valid middleIndex.

Constraints:
    1 <= nums.length <= 100
    -1000 <= nums[i] <= 1000

A:
    empty nums      ->  not possible due to constraint
    nums of size 1  ->  if nums=[0] return 0 else -1
    negative nums   ->  possble

D:
    Input: nums = [2,3,-1,8,4]
    mid = 0
    left = sum(nums[:mid]) = 0
    right = sum(nums[mid+1:]) = 3+-1+8+4 != 0

    mid = 1
    left = sum(nums[:1]) = 2
    right = sum(nums[1+1:]) = 3+-1+8+4 != 2

    mid = 2
    left = sum(nums[:2]) = 5
    right = sum(nums[1+2:]) = 8+4 != 5

    mid = 3
    left = sum(nums[:3]) = 4
    right = sum(nums[1+3:]) = 4 == 4
"""


class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        for index in range(len(nums) - 1):
            if sum(nums[:index]) == sum(nums[index + 1 :]):
                return index

        if len(nums) == 1:
            return 0

        if sum(nums[1:]) == 0:
            return 0

        if sum(nums[:-1]) == 0:
            return len(nums) - 1

        return -1


cases = [
    ([2, 3, -1, 8, 4], 3),
    ([1, -1, 4], 2),
    ([2, 5], -1),
    ([0], 0),
    ([1, -1, 1], 0),
    ([-1, 1, 10], 2),
    ([1], 0),
]

sol = Solution()
for (nums, exp) in cases:
    assert (
        got := sol.findMiddleIndex(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
