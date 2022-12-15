"""Given a collection of numbers that might contain duplicates, return all possible unique
permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute(nums, set())

    def permute(self, nums, usedElements):
        if len(nums) < 2:
            return [nums]
        if len(nums) == 2:
            return [nums, nums[::-1]] if nums[0] != nums[1] else [nums]

        perms = []
        for i in range(len(nums)):
            if nums[i] in usedElements:
                continue

            usedElements.add(nums[i])
            for p in self.permuteUnique(nums[:i] + nums[i + 1 :]):
                perms.append(tuple([nums[i]]) + tuple(p))
        return perms


sol = Solution()
seq = [1, 1, 2]
print("Permuting: ", seq)
print(" ans: ", sol.permuteUnique(seq))
print("-------------------------------------")

seq = [1, 1]
print("Permuting: ", seq)
print(" ans: ", sol.permuteUnique(seq))
print("-------------------------------------")

seq = [1, 1, 1, 1, 1, 1, 1, 4]
print("Permuting: ", seq)
print(" ans: ", sol.permuteUnique(seq))
print("-------------------------------------")
