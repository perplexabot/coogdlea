"""
You are given an array of positive integers nums and want to erase a subarray containing unique
elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is,
if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example 1:
    Input: nums = [4,2,4,5,6]
    Output: 17
    Explanation: The optimal subarray here is [2,4,5,6].

Example 2:
    Input: nums = [5,2,1,2,5,2,1,2,5]
    Output: 8
    Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 104

URL: https://leetcode.com/problems/maximum-erasure-value/

m = float('-inf')
for i, num in enum(nums):
    if num in curr:
        m = max(m, sum(curr))
        curr = set(nums[ind[num]+1:i])
    ind[num] = i
    curr.add(num)

return max(m, sum(curr))
"""


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        ind = {}
        curr = set()
        sums = []

        for i, num in enumerate(nums):
            if num in curr:
                sums.append(curr)
                curr.remove(nums[ind[num] + 1 : i]))
            ind[num] = i
            curr.add(num)
        sums.append(curr)

        return max(sum(s) for s in sums)


inps = [
    ([4, 2, 4, 5, 6], 17),
    ([5, 2, 1, 2, 5, 2, 1, 2, 5], 8),
    ([1], 1),
    ([1, 2], 3),
    ([1, 1], 1),
    ([1, 3, 1, 3], 4),
    ([5, 4, 1], 10),
]

sol = Solution()
for inp, exp in inps:
    assert (
        got := sol.maximumUniqueSubarray(inp)
    ) == exp, f"failed with {inp}, expecting {exp}, got {got}"
