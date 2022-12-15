"""Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return [nums, nums[::-1]] if len(nums) == 2 else nums
        return [
            [nums[i]] + p for i in range(len(nums)) for p in self.permute(nums[:i] + nums[i + 1 :])
        ]


sol = Solution()

seq = [1, 2, 3]
print("Permuting: ", seq)
print(" Got: ", sol.permute(seq))
print("------------------------")

seq = [1]
print("Permuting: ", seq)
print(" Got: ", sol.permute(seq))
print("------------------------")
