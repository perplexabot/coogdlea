"""
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
    For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.

Given an integer array nums, choose four distinct indices w, x, y, and z such that the product
    difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

Example 1:
    Input: nums = [5,6,2,7,4]
    Output: 34
    Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for
        the second pair (2, 4).
    The product difference is (6 * 7) - (2 * 4) = 34.

Example 2:
    Input: nums = [4,2,5,9,7,4,8]
    Output: 64
    Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for
        the second pair (2, 4).
    The product difference is (9 * 8) - (2 * 4) = 64.

Constraints:
    4 <= nums.length <= 10^4
    1 <= nums[i] <= 10^4

A:
    can ints be negative or zero?                   no!
    can list be empty?                              no
    can you use the same int more than once?        assuming not (no, "distinct")

D:
    Input: nums = [5,6,2,7,4]
    max0: 7
    max1: 6
    min0: 2
    min1: 4
    ans:    (7*6) - (4*2) = 34

P:
    pick largest two ints
    pick smallest two ints
    return diff
"""


# modifying input array, can make copy instead.
def maxProductDifference(nums: list[int]) -> int:
    nums.sort()
    return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


cases = [
    ([5, 6, 2, 7, 4], 34),
    ([4, 2, 5, 9, 7, 4, 8], 64),
    ([1, 1, 1, 1], 0),
    ([1, 2, 3, 4], 10),
    ([1, 1, 2, 2], 3),
]

for (nums, exp) in cases:
    assert (
        got := maxProductDifference(nums)
    ) == exp, f"Failed ({nums}) - expecting ({exp}), got ({got})"
