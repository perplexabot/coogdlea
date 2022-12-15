"""Given an array of non-negative integers, you are initially positioned at the first index
of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 2:
            return True

        if 0 not in nums:
            return True

        def dfs(ind, found):
            if ind == len(nums) - 1:
                found.add(True)
            if ind < len(nums) - 1 and nums[ind] != 0:
                for i in range(1, nums[ind] + 1):
                    dfs(ind + i, found)

        bool_set = set()
        dfs(0, bool_set)
        return True if True in bool_set else False


sol = Solution()
inps = [
    [2, 3, 1, 1, 4],
    [3, 2, 1, 0, 4],
    [0, 0, 0, 0, 0],
    [0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0],
    [2, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0],
    [2, 0, 3, 0, 0, 5, 0, 0, 0, 0],
]
for inp in inps:
    print("Doing: ", inp)
    ans = sol.canJump(inp)
    print(" got: ", ans)
