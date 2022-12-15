"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""


class Solution:
    def findMin(self, nums: 'List[int]') -> int:
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        def helper(s, e):
            if e - s <= 1:
                return nums[e]

            p = s + ((e - s) // 2)
            pl = s + ((p - s) // 2)
            pr = e - ((e - p) // 2)

            if nums[p] < nums[pl]:
                return helper(pl, p)
            elif nums[p] > nums[pr]:
                return helper(p, pr)
            else:
                a = helper(s, pl)
                b = helper(pr, e)
                c = helper(pl, p)
                d = helper(p, pr)
                return min(a, b, c, d)

        return helper(0, len(nums) - 1)


inps = [
    ([2, 2, 2, 0, 2, 2], 0),
    ([1, 3, 5], 1),
    ([2, 2, 2, 0, 1], 0),
    ([2, 2, 2, 0, 1, 2, 2], 0),
    ([2, 2, 2, 2, 2, 2, 0], 0),
    ([1], 1),
    ([], None),
    ([2, 2, 2, 2, 2, 2, 2, 2], 2),
    ([1, 2], 1),
    ([2, 1], 1),
    ([5, 1, 2], 1),
    ([1, 2, 5], 1),
    ([1, 1, 1], 1),
    ([1, 1], 1),
]

sol = Solution()
for n, exp in inps:
    print(f"Finding min in {n} and asserting...")
    ans = sol.findMin(n)
    assert ans == exp, f"ans: {ans}, exp: {exp}"
