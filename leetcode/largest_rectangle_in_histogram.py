"""Given n non-negative integers representing the histogram's bar height where the width of each
bar is 1, find the area of largest rectangle in the histogram.

Example:
Input: [2,1,5,6,2,3]
Output: 10
"""


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        def getLeftArea(i):
            e = heights[i]
            l = 0
            j = i - 1
            while j >= 0 and heights[j] >= e:
                l += 1
                j -= 1
            return e * l

        def getRightArea(i):
            e = heights[i]
            l = 0
            j = i + 1
            while j < len(heights) and heights[j] >= e:
                l += 1
                j += 1
            return e * l

        i = 0
        maxArea = float('-inf')
        while i < len(heights):
            l = getLeftArea(i)
            r = getRightArea(i)
            maxArea = max(maxArea, l + r + heights[i])
            i += 1
        return maxArea


inps = [
    ([2, 1, 5, 6, 2, 3], 10),
    ([5, 4, 3, 2, 1], 9),
    ([1, 1, 1, 1], 4),
    ([1, 0, 2, 0, 4, 0, 2, 0, 1], 4),
    ([1, 2, 3, 4, 5], 9),
    ([], 0),
    ([5], 5),
    ([1, 2, 3, 4, 3, 2, 1], 10),
    ([1, 2, 3, 0, 3, 2, 1], 4),
    ([10, 1, 1], 10),
    ([5, 1, 1, 1, 1, 1, 1], 7),
]

sol = Solution()
for inp, exp in inps:
    print(f"Finding max area for {inp} and asserting...")
    assert exp == sol.largestRectangleArea(inp)
