"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the
    ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the
    lowest of the k scores is minimized.

Return the minimum possible difference.

Example 1:
    Input: nums = [90], k = 1
    Output: 0
    Explanation: There is one way to pick score(s) of one student:
    - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
    The minimum possible difference is 0.

Example 2:
    Input: nums = [9,4,1,7], k = 2
    Output: 2
    Explanation: There are six ways to pick score(s) of two students:
    - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
    - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
    - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
    - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
    - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
    - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
    The minimum possible difference is 2.

Constraints:
    1 <= k <= nums.length <= 1000
    0 <= nums[i] <= 10**5

A:
    empty list ->   not possible
    k > len(nums)   ->  not possible
    k = 1 -> return 0
    non ints in arr -> not possible
    negative nums in arr -> not possible
    k = len(arr) -> sort(arr), then arr[-1] - arr[0]

D:
    arr.sort()
    s = 0
    e = s + k - 1
    ans = float('inf')
    while e < len(arr):
        ans = min(ans, arr[e] - arr[s])
        s += 1
        e += 1
    return ans
"""


class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        s = 0
        e = s + k - 1
        ans = float('inf')
        while e < len(nums):
            ans = min(ans, nums[e] - nums[s])
            s += 1
            e += 1
        return ans


cases = [([90], 1, 0), ([9, 4, 1, 7], 2, 2)]

sol = Solution()
for (nums, k, exp) in cases:
    assert (
        got := sol.minimumDifference(nums, k)
    ) == exp, f"Failed case ({nums}, {k}) - expecting ({exp}), got ({got})."
