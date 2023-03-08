"""
A sequence of numbers is called an arithmetic progression if the difference between any two
    consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic
    progression. Otherwise, return false.

Example 1:
    Input: arr = [3,5,1]
    Output: true
    Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2
        respectively, between each consecutive elements.

Example 2:
    Input: arr = [1,2,4]
    Output: false
    Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:
    2 <= arr.length <= 1000
    -106 <= arr[i] <= 106

A:
    arr is empty: return true (not possible)
    arr len is 1: return true (not possible)
    arr len is 2: return true

D:
    sort
    compare conseq
    break at first unequal and return False
    return True
"""

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        i = 1
        diffs = set()
        while i < len(arr):
            diffs.add(arr[i] - arr[i - 1])
            i += 1

        return len(diffs) == 1


cases = [([3, 5, 1], True), ([1, 2, 4], False)]

sol = Solution()
for (arr, exp) in cases:
    assert (
        got := sol.canMakeArithmeticProgression(arr)
    ) == exp, f"Failed case ({arr}) - expecting ({exp}), got ({got})."
