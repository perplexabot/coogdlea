"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100

A:
    empty nums  ->  return 0

D:
    nums = [1,2,3,1,1,3] 
    cnt = {1:3, 2:1, 3:2}
    return 3C2 + 2C2 = (3!)/(2!1!) + (2!)/(2!0!) = (6/2) + (2/2) = 4
"""


def numIdenticalPairs(nums: list[int]) -> int:
    if not nums:
        return 0

    from collections import Counter
    from math import factorial

    cnts = Counter(nums)
    return sum(factorial(cnt) // (2 * factorial(cnt - 2)) for cnt in cnts.values() if cnt > 1)


cases = [
    ([1, 2, 3], 0),
    ([1, 2, 3, 1, 1, 3], 4),
    ([1, 1, 1, 1], 6),
    ([], 0),
    ([1], 0),
    ([1, 1], 1),
    ([1, 2, 1], 1),
    ([1, 1, 2], 1),
    ([2, 1, 1], 1),
    ([1, 2, 3, 1, 1, 3], 4),
]

for (nums, exp) in cases:
    assert (
        got := numIdenticalPairs(nums)
    ) == exp, f"Assert fail with ({nums}) - expecting ({exp}), got ({got})"
