"""
You are given an integer array nums with the following properties:
    nums.length == 2 * n.
    nums contains n + 1 unique elements.
    Exactly one element of nums is repeated n times.

Return the element that is repeated n times.

Example 1:
    Input: nums = [1,2,3,3]
    Output: 3

Example 2:
    Input: nums = [2,1,2,5,3,2]
    Output: 2

Example 3:
    Input: nums = [5,1,5,2,5,3,5,4]
    Output: 5

Constraints:
    2 <= n <= 5000
    nums.length == 2 * n
    0 <= nums[i] <= 10^4
    nums contains n + 1 unique elements and one of them is repeated exactly n times.

A:
    empty arr   ->  []
    len(arr) == 2   ->  n == 1  ->  either element

D:
    Input: nums = [5,1,5,2,5,3,5,4]
    len(nums) = 8, n = 4
    cnts = {}
    5 -> {5:1}
    1 -> {5:1, 1:1}
    5 -> {5:2, 1:1}
    2 -> {5:2, 1:1, 2:1}
    5 -> {5:3, 1:1, 2:1}
    3 -> {5:3, 1:1, 2:1, 3:1}
    5 -> {5:4, 1:1, 2:1, 3:1} 5 hit n   -> return 5

P:
    get n
    for num in nums:
        cnts[num] += 1
        if cnts[num] == n:
            return cnts[num]
"""


def repeatedNTimes(nums: list[int]) -> int:
    from collections import defaultdict

    n = len(nums) // 2
    cnts = defaultdict(int)
    for num in nums:
        cnts[num] += 1
        if cnts[num] == n:
            return num


cases = [
    ([1, 2], 1),
    ([1, 1, 2, 3], 1),
    ([2, 3, 1, 1], 1),
    ([1, 2, 3, 3], 3),
    ([2, 1, 2, 5, 3, 2], 2),
    ([5, 1, 5, 2, 5, 3, 5, 4], 5),
]

for (case, exp) in cases:
    assert (
        got := repeatedNTimes(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
