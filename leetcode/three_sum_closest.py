# Given an array nums of n integers and an integer target, find three integers in 
# nums such that the sum is closest to target. Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
# Example:
#     Given array nums = [-1, 2, 1, -4], and target = 1.
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

def threeSumClosest(nums, target):
    nums.sort()
    threeSum = float('inf')
    ln = len(nums)

    def twoSumClosest(nums, target):
        L = 0
        R = len(nums) - 1
        twoSum = float('inf')
        while L < R:
            t = nums[L] + nums[R]
            difft = abs( t - target )
            if difft < abs( twoSum - target ):
                if not difft:
                    return t
                twoSum = t

            if t < target:
                while nums[L] == nums[L+1] and L+1 < len(nums) - 1:
                    L += 1
                else:
                    L += 1
            else:
                while nums[R] == nums[R-1] and R-1 > 0:
                    R -= 1
                else:
                    R -= 1
        return twoSum

    if ln < 3:
        return None
    else:
        for i in range(ln-2):
            if nums[i] == nums[i-1] and i > 0:
                continue

            potentialSum = nums[i] + twoSumClosest( nums[i+1:], target - nums[i] ) 
            potDiff = abs( potentialSum - target ) 

            if not potDiff:
                return potentialSum

            if potDiff < abs( threeSum - target ):
                threeSum = potentialSum

        return threeSum
