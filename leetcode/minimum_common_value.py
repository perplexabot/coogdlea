"""
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum
    integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one
    occurrence of that integer.

Example 1:
    Input: nums1 = [1,2,3], nums2 = [2,4]
    Output: 2
    Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:
    Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
    Output: 2
    Explanation: There are two common elements in the array 2 and 3 out of which 2 is the
        smallest, so 2 is returned.

Constraints:
    1 <= nums1.length, nums2.length <= 105
    1 <= nums1[i], nums2[j] <= 109
    Both nums1 and nums2 are sorted in non-decreasing order.

A:
    one arr is empty -> return -1
    both empty -> return -1

D:
    convert to sets
    take intersection
    return min
"""

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set.intersection(set(nums1), set(nums2)), default=-1)


cases = [
    ([1, 2, 3], [2, 4], 2),
    ([1, 2, 3, 6], [2, 3, 4, 5], 2),
    ([], [1], -1),
    ([1], [], -1),
    ([1], [2], -1),
    ([-1, 100], [-1, 200], -1),
    ([1, 2], [1, 2], 1),
]

sol = Solution()
for (nums1, nums2, exp) in cases:
    assert (
        got := sol.getCommon(nums1, nums2)
    ) == exp, f"Failed case ({nums1}, {nums2}) - expecting ({exp}), got ({got})."
