"""Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        max_left = {0: height[0]}
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i])

        max_right = {len(height) - 1: height[-1]}
        for i in reversed(range(0, len(height) - 1)):
            max_right[i] = max(max_right[i + 1], height[i])

        tot = 0
        for i in range(1, len(height) - 1):
            left_max = max_left[i]
            right_max = max_right[i]
            min_max = min(left_max, right_max)
            tot += min_max - height[i]
        return tot


inps = [
    ([1, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([0, 1, 0, 1, 0, 1, 0, 1, 0], 3),
    ([2, 1, 1, 1, 1, 1, 2], 5),
    ([3, 2, 0, 0, 1, 4], 9),
    ([1, 1, 1, 1, 1, 1, 1, 1], 0),
    ([0, 0, 0, 0, 0, 0], 0),
    ([1, 0, 1], 1),
    ([], 0),
    ([1], 0),
    ([0], 0),
    ([1, 2, 3, 2, 1], 0),
    ([0, 1, 2, 3, 2, 1, 0], 0),
    ([1, 2, 3, 0, 3, 2, 1], 3),
    ([1, 2, 3, 0, 0, 0, 3, 2, 1], 9),
    ([1, 1, 1, 1, 0, 1, 1, 1, 1], 1),
    ([1, 1, 1, 1, 0, 1], 1),
    ([1, 1, 1, 1, 1, 0], 0),
    ([3, 2, 1, 0, 1, 2, 3], 9),
    ([3, 2, 1, 0, 1, 1, 3], 10),
    ([3, 3, 3, 2, 2, 1, 0, 1, 2, 2, 3, 3, 3], 11),
    ([3, 0, 2, 0, 1, 0, 1, 0, 2, 0, 3], 21),
    ([3, 3, 0, 2, 2, 0, 1, 1, 0, 1, 1, 0, 2, 2, 0, 3, 3], 27),
    ([1, 0, 1, 1, 1, 1, 1, 1, 0, 1], 2),
]
sol = Solution()
for inp, exp in inps:
    print(f"Calcluating water trapped for {inp} and asserting...")
    ans = sol.trap(inp)
    print(f' Got: {ans}')
    assert exp == ans
print("*** PASSED! ***")
