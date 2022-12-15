def fourSum(nums, target):
    def twoSum(nums, target):
        L = 0
        R = len(nums) - 1
        l2 = []
        while L < R:
            twoSum = nums[L] + nums[R]
            if twoSum == target:
                l2.append( [ nums[L], nums[R] ] )
                if nums[L] == nums[L+1]:
                    while nums[L] == nums[L+1] and L+1 < R:
                        L += 1
                    else:
                        L += 1
                else:
                    while nums[R] == nums[R-1] and R-1 > L:
                        R -= 1
                    else:
                        R -= 1
            elif twoSum < target:
                L += 1
            else:
                R -= 1
        
        return l2

    def threeSum(nums, target):
        l3 = []
        for i in range(len(nums) - 2):
            if nums[i] == nums[i-1] and i > 0:
                continue

            l2 = twoSum(nums[i+1:], target-nums[i])
            for pair in l2:
                l3.append([nums[i], pair[0], pair[1]])
        return l3

    nums.sort()
    l4 = []
    for i in range(len(nums) - 3):
        if nums[i] == nums[i-1] and i > 0:
            continue
        l3 = threeSum(nums[i+1:], target-nums[i])
        for trips in l3:
            l4.append([nums[i], trips[0], trips[1], trips[2]])
    return l4
