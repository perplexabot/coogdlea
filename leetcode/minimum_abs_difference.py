"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute
difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
    - a, b are from arr
    - a < b
    - b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
    Input: arr = [4,2,1,3]
    Output: [[1,2],[2,3],[3,4]]
    Explanation: The minimum absolute difference is 1. List all pairs with difference equal
        to 1 in ascending order.

Example 2:
    Input: arr = [1,3,6,10,15]
    Output: [[1,3]]

Example 3:
    Input: arr = [3,8,-10,23,19,-4,-14,27]
    Output: [[-14,-10],[19,23],[23,27]]

Constraints:
    2 <= arr.length <= 105
    -10**6 <= arr[i] <= 10**6

A:
    arr is empty    ->  not possible
    arr.len = 1     -> not possible
    arr has repeated elems  ->  abs diff is 0
    what about [1,1,1]  ->   is it just [[1,1]] or [[1,1],[1,1]]? neither, a has to be < b

D:
    Input: arr = [4,2,1,3]
    sarr = [1,2,3,4], mindiff = inf, found = []

    ind = 0
    currdiff = abs(sarr[ind+1] - sarr[ind])
    if currdiff < minddiff:
        found = [[sarr[ind+1], sarr[ind]]
        mindiff = currdiff
    elif currdiff == mindiff
        found.append([sarr[ind+1], sar[ind]])
"""


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        mindiff = float('inf')
        found = []
        for ind in range(len(arr) - 1):
            currdiff = abs(arr[ind] - arr[ind + 1])
            if currdiff < mindiff:
                found = [[arr[ind], arr[ind + 1]]]
                mindiff = currdiff
            elif currdiff == mindiff:
                found.append([arr[ind], arr[ind + 1]])
        return found


cases = [
    ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
    ([1, 3, 6, 10, 15], [[1, 3]]),
    ([3, 8, -10, 23, 19, -4, -14, 27], [[-14, -10], [19, 23], [23, 27]]),
]


sol = Solution()
for (arr, exp) in cases:
    assert (
        got := sol.minimumAbsDifference(arr)
    ) == exp, f"Failed case ({arr}) - got ({got}), expecting ({exp})."
