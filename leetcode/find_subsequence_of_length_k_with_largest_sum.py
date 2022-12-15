"""
You are given an integer array nums and an integer k. You want to find a subsequence of nums of
    length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements
    without changing the order of the remaining elements.

Example 1:
    Input: nums = [2,1,3,3], k = 2
    Output: [3,3]
    Explanation:
    The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
    Input: nums = [-1,-2,3,4], k = 3
    Output: [-1,3,4]
    Explanation:
    The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
    Input: nums = [3,4,3,3], k = 2
    Output: [3,4]
    Explanation:
    The subsequence has the largest sum of 3 + 4 = 7.
    Another possible subsequence is [4, 3].

Constraints:
    1 <= nums.length <= 1000
    -10**5 <= nums[i] <= 10**5
    1 <= k <= nums.length

A:
    k larger than nums length or less than 0 -> not possible according to constraints
    empty nums -> return []
    len(nums) == k -> return nums
    k = 0 -> return []
    elements of nums not ints -> not possible according to constraints
    k not an int -> not possible according to constraints
D:
    if k > len(nums): return []
    if k == len(nums_: return nums
    nums = [2,1,3,3], k = 2
    maxes = nums[:k]
    for i in nums[k:]:
        if i > min(maxes):
            maxes.insert(maxes.index(min(maxes)), i)
    return sum(maxes)
"""


def maxSubsequence(nums: list[int], k: int) -> list[int]:
    if k > len(nums) or k == 0:
        return []
    if k == len(nums):
        return nums

    maxes = nums[:k]
    for i in nums[k:]:
        if i > min(maxes):
            maxes.remove(min(maxes))
            maxes.append(i)
    return maxes


def maxSubsequence_better(nums: list[int], k: int) -> list[int]:
    if k > len(nums) or k == 0:
        return []
    if k == len(nums):
        return nums

    from collections import Counter

    cnts = Counter(nums[:k])
    for i in nums[k:]:
        currm = min(cnts)
        if i > currm:
            if cnts[currm] == 1:
                cnts.pop(currm)
            elif cnts[currm] > 1:
                cnts[currm] -= 1
            cnts[i] += 1

    size = 0
    final = []
    for i in nums:
        if i in cnts:
            if cnts[i] > 0:
                cnts[i] -= 1
                final.append(i)
                size += 1
            else:
                cnts.pop(i)
        if size == k:
            break

    return final


cases = [
    ([2, 1, 3, 3], 2, [3, 3]),
    ([-1, -2, 3, 4], 3, [-1, 3, 4]),
    ([3, 4, 3, 3], 2, [3, 4]),
    ([], 3, []),
    ([1], 10, []),
    ([1], 1, [1]),
    ([1, 2], 1, [2]),
    ([1, 2], 2, [1, 2]),
    ([1, 2, 34], 1, [34]),
    ([1, 2, 3], 0, []),
]

for (nums, k, exp) in cases:
    assert (
        ans := maxSubsequence_better(nums, k)
    ) == exp, f"Failed with ({nums},{k}) - got ({ans}), expecting ({exp})"
