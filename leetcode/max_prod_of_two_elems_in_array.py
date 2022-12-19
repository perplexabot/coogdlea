"""
Given the array of integers nums, you will choose two different indices i and j of that array.
    Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:
    Input: nums = [3,4,5,2]
    Output: 12
    Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum
        value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

Example 2:
    Input: nums = [1,5,4,5]
    Output: 16
    Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum
        value of (5-1)*(5-1) = 16.

Example 3:
    Input: nums = [3,7]
    Output: 12

Constraints:
    2 <= nums.length <= 500
    1 <= nums[i] <= 10^3

A:
    empty nums      ->  return 0
    len(nums) == 1  ->  return 0
    nums only has positive ints according to constraints

D:
    [3,4,5,2]
    if len(nums) < 2: return 0
    max0 = nums[0] = 3
    max1 = nums[1] = 4
    5 > min(max0,max1) -> max0 < max1 -> max0 = 5, max0=5 max1=4
    2 < min(max0,max1)
    return (5-1)(4-1) = 12
"""


def maxProduct(nums: list[int]) -> int:
    if len(nums) < 2:
        return 0

    max0, max1 = nums[:2]

    for n in nums[2:]:
        if n > min(max0, max1):
            if max0 < max1:
                max0 = n
            else:
                max1 = n
    return (max0 - 1) * (max1 - 1)


cases = [
    ([3, 4, 5, 2], 12),
    ([1, 5, 4, 5], 16),
    ([3, 7], 12),
    ([], 0),
    ([1], 0),
    ([1, 2], 0),
    ([1, 1], 0),
    ([10, 1, 10], 81),
    ([10, 10, 1], 81),
    ([1, 10, 10], 81),
    ([2, 1, 2, 1], 1),
]

for (nums, exp) in cases:
    assert (
        got := maxProduct(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})"
