"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing
    subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it
    is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and
    for each l <= i < r, nums[i] < nums[i + 1].

Example 1:
    Input: nums = [1,3,5,4,7]
    Output: 3
    Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
    Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and
        7 are separated by element 4.

Example 2:
    Input: nums = [2,2,2,2,2]
    Output: 1
    Explanation: The longest continuous increasing subsequence is [2] with length 1. Note
        that it must be strictly increasing.

Constraints:
    1 <= nums.length <= 10**4
    -10**9 <= nums[i] <= 10**9

A:
    nums is empty       ->  retrun 0
    nums len is 1       ->  return 1
    none num is nums    ->  fail (constraint says not possible)
D:
            0 1 2 3 4
    nums = [1,3,5,4,7]
    s=0,f=1, nums[f] > nums[f-1]
    s=0,f=2, nums[f] > nums[f-1]
    s=0,f=3, nums[f] < nums[f-1] -> max_sub = max(max_sub, f-s), s = f, f = s+1
    s=3,f=4, nums[f] > nums[f-1]
    s=3,f=5, f >= len(nums) -> max_sub = max(max_sub, f-s)

P:
    if len(nums) < 2:
        return 1 if nums else 0
    s=0
    while s < len(nums)-1:
        f = s+1
        while f < len(nums) and nums[f] > nums[s]:
            f += 1
        max_sub = max(max_sub,(f-1)-s))
        s = f
"""


def findLengthOfLCIS(nums: list[int]) -> int:
    if len(nums) < 2:
        return 1 if nums else 0

    max_sub = float('-inf')
    s = 0
    while s < len(nums) - 1:
        curr = s + 1
        e = s
        while curr < len(nums) and nums[curr] > nums[curr - 1]:
            curr += 1
            e += 1
        max_sub = max(max_sub, e - s + 1)
        s = curr
    return max_sub


cases = [
    ([1, 3, 5, 4, 7], 3),
    ([2, 2, 2, 2, 2], 1),
    ([], 0),
    ([1], 1),
    ([1, 0, -3], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3),
    ([-1, 0, 1], 3),
]

for (nums, exp) in cases:
    assert (
        ans := findLengthOfLCIS(nums)
    ) == exp, f"Failed with ({nums}) - expecting ({exp}), got ({ans})"
