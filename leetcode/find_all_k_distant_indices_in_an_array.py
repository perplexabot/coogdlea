"""
You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an
    index i of nums for which there exists at least one index j such that |i - j| <= k
    and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.

Example 1:
                   0 1 2 3 4 5 6
    Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
    Output: [1,2,3,4,5,6]
    Explanation: Here, nums[2] == key and nums[5] == key.
    - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and
        nums[j] == key. Thus, 0 is not a k-distant index.
    - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
    - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
    - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
    - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
    - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
    - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
    Thus, we return [1,2,3,4,5,6] which is sorted in increasing order.

Example 2:
    Input: nums = [2,2,2,2,2], key = 2, k = 2
    Output: [0,1,2,3,4]
    Explanation: For all indices i in nums, there exists some index j such that |i - j| <= k
        and nums[j] == key, so every index is a k-distant index.
    Hence, we return [0,1,2,3,4].

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000
    key is an integer from the array nums.
    1 <= k <= nums.length

A:
    len(nums) = 0   ->  not possible
    len(nums) = 1   ->  return 0
    len(nums) > 1   ->  run check
    if k = 0        ->  not possible

D:
    Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1

    ans = {}
    3
    4
    9   -> ans.append(curr_index), ans.append(range(curr_index - k, curr_index + k +1))
    1
    3
    9   -> ans.append(curr_index), ans.append(range(curr_index - k, curr_index +k + 1))

    final = {i for i in ans if i > -1 and i < len(nums)}
"""


class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        ans = []
        for (index, element) in enumerate(nums):
            if element == key:
                ans.extend(list(range(index - k, index + k + 1)))

        final = [e for e in ans if e > -1 and e < len(nums)]
        return list(set(final))


cases = [
    ([3, 4, 9, 1, 3, 9, 5], 9, 1, [1, 2, 3, 4, 5, 6]),
    ([2, 2, 2, 2, 2], 2, 2, [0, 1, 2, 3, 4]),
    ([1], 1, 1, [0]),
    ([1], 5, 1, []),
    ([1], 1, 4, [0]),
]

sol = Solution()
for (nums, key, k, exp) in cases:
    assert (
        got := sol.findKDistantIndices(nums, key, k)
    ) == exp, f"Failed case ({nums}, {key}, {k}) - expecting ({exp}), got ({got})."
