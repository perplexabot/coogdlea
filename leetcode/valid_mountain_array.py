"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
    Input: arr = [2,1]
    Output: false

Example 2:
    Input: arr = [3,5,5]
    Output: false

Example 3:
    Input: arr = [0,3,2,1]
    Output: true

Constraints:
    1 <= arr.length <= 10**4
    0 <= arr[i] <= 10**4

A:
    len(arr) < 3    ->  return false

D:
    if length(arr) < 3:
        return false

    if arr[1] < arr[0]:
        return false

    curr = 2
    while arr[curr] > arr[curr-1]:
        curr += 1
        if curr == length(arr):
            return False

    while arr[curr] < arr[curr-1]:
        curr += 1
        if curr == length(arr):
            return True

    return False
"""


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        if arr[1] <= arr[0]:
            return False

        curr = 2
        while arr[curr] > arr[curr - 1]:
            curr += 1
            if curr == len(arr):
                return False

        while arr[curr] < arr[curr - 1]:
            curr += 1
            if curr == len(arr):
                return True

        return False


cases = [
    ([2, 1], False),
    ([3, 5, 5], False),
    ([0, 3, 2, 1], True),
    ([1], False),
    ([1, 2], False),
    ([1, 2, 1], True),
    ([1, 2, 2], False),
    ([2, 2, 1], False),
    ([1, 1, 1], False),
    ([1, 1, 2, 1], False),
    ([0, 1, 2, 3, 2], True),
    ([1, 2, 3, 2, 1, 0], True),
    ([1, 2, 3, 2, 1, 1], False),
]

sol = Solution()
for (arr, exp) in cases:
    assert (
        got := sol.validMountainArray(arr)
    ) == exp, f"Failed case ({arr}) - expecting ({exp}), got ({got})."
