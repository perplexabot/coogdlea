"""Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and
conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        left, right = 0, 1
        maxSum = nums[0]
        currSum = maxSum
        while right < len(nums):
            currSum = sum([currSum, nums[right]])
            if nums[right] > currSum:
                left = right
                currSum = nums[left]
                maxSum = max(nums[right], maxSum)
            else:
                maxSum = max(maxSum, currSum)
            right += 1
        return maxSum


sol = Solution()
inputs = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [-50, 4, 3, -1, 5, 10, -2],
    [1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [-1, 1, -1, 1, -1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, -1, 0, 1],
    [0, -1],
]

for inp in inputs:
    print("Trying: ", inp)
    ans = sol.maxSubArray(inp)
    print(" Got: ", ans)
