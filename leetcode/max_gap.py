"""
Given an unsorted array, find the maximum difference between the successive elements in its
sorted form.  Return 0 if the array contains less than 2 elements.

Example 1:
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Note:
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed
integer range.
Try to solve it in linear time/space.
"""


class Solution:
    def maximumGap(self, nums: 'List[int]') -> int:
        if len(nums) < 2:
            return 0

        def radixSort(lst, cnt=1, iters=0):
            if iters == max_digs:
                return lst
            lst.sort(key=lambda x: (x // cnt) % 10)
            return radixSort(lst, cnt * 10, iters + 1)

        max_digs = len(str(max(nums)))
        snums = radixSort(nums)

        gap = float('-inf')
        for j in range(1, len(snums)):
            gap = max(snums[j] - snums[j - 1], gap)
        return gap


inps = [
    ([3, 6, 9, 1], 3),
    ([10], 0),
    ([], 0),
    ([1, 2, 3, 4, 5, 6], 1),
    ([2, 6, 10, 8, 20, 10], 10),
    ([0, 5000], 5000),
]

sol = Solution()
for nums, exp in inps:
    print(f"Finding max gap in {nums} and asserting...")
    ans = sol.maximumGap(nums)
    assert ans == exp, f"ans: {ans}, exp = {exp}"
