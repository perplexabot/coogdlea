"""
Given an binary array nums and an integer k, return true if all 1's are at least k places away from
    each other, otherwise return false.

Example 1:
    Input: nums = [1,0,0,0,1,0,0,1], k = 2
    Output: true
    Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
    Input: nums = [1,0,0,1,0,1], k = 2
    Output: false
    Explanation: The second 1 and third 1 are only one apart from each other.

Constraints:
    1 <= nums.length <= 105
    0 <= k <= nums.length
    nums[i] is 0 or 1

A:
    k is negative   -> return false
    list is empty   -> return true
    k is zero       -> set(nums) == {1}
    list has no 1s  -> true
    consider odd and even number of 1s?

D:
nums    1   0   0   0   1   0   0   1
c       0   1   2   3   |   1   2   |
                    |           |
                  c >= k      c >= k
                 continue    continue
                reset c=0   reset c=0

    or

nums    1   0   0   0   1   0   0   1
index   0   1   2   3   4   5   6   7

    1_index_list = [0, 4, 7]
    diffs = [4 - 0, 7 - 4] = [4, 3]
    places = [x-1 for x in diffs]
    return all(x >= k for x in places)
"""


def kLengthApart(nums: list[int], k: int) -> bool:
    if k < 0:
        return False

    if not nums:
        return True

    one_inds = [index for index, num in enumerate(nums) if num == 1]
    diffs = (
        []
        if len(one_inds) == 1
        else [one_inds[i] - one_inds[i - 1] - 1 for i in range(1, len(one_inds))]
    )
    return all(x >= k for x in diffs)


cases = [
    ([1, 0, 0, 0, 1, 0, 0, 1], 2, True),
    ([1, 0, 0, 1, 0, 1], 2, False),
    ([1, 2, 1], -1, False),
    ([], 3, True),
    ([], 0, True),
    ([1, 0, 1], 0, True),
    ([1, 1], 0, True),
    ([1, 1, 2], 0, True),
    ([0, 1, 1, 0], 0, True),
    ([0, 0, 3, 0], 3, True),
    ([1], 10, True),
    ([0], 3, True),
    ([1, 0, 1], 5, False),
]

for (nums, k, exp) in cases:
    assert (
        ans := kLengthApart(nums, k)
    ) == exp, f"Failed ({nums}, {k}) - expecting ({exp}), got ({ans})"
