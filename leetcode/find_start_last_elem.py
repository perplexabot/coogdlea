"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# Find an occurence of target with bin search
# search left segment for left most element:
#   find first number not equal to tgt with next elem equal to tgt
#   use bin search to find this number
#       if piv != tgt and piv+1=tgt:
#           return piv+1
#       if piv == 0 or piv == len(lst):
#           return piv
#       if piv == tgt:
#           search left segment
#       else:
#           search right segment
# search right segment for right most element:
#   similar to left side

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect(nums, target) - 1
        if not nums or nums[left] != target:
            return [-1, -1]

        return [left, right]
