"""Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        c = Counter(nums)
        return max(c.items(), key=lambda x: x[1])[0]


inps = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([1, 7, 7, 7], 7),
    ([1, 2, 1, 3, 1, 4, 1, 5], 1),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 0),
]

sol = Solution()
for l, exp in inps:
    print(f"Getting majority elem for {l} and asserting...")
    assert exp == sol.majorityElement(l)
