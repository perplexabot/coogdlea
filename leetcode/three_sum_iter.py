def threeSum(nums):
    def twoSum(l, k):
        l2 = []
        L = 0
        R = len(l)-1
        while L < R:
            s = l[L] + l[R]
            if s == k:
                l2.append( [ l[L], l[R] ] )
                while l[L] + l[R] == k and L < R:
                    L += 1
            elif s < k:
                L += 1
            else:
                R -= 1
        return l2

    
    nums = sorted(nums)
    l3 = []
    for i in range(len(nums) - 2):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        a = nums[i]
        l2 = twoSum(nums[i+1:], -a)
        for pair in l2:
            l3.append([a, *pair])

    sl3 = [ tuple( sorted(x) ) for x in l3 ]
    l3Set = set(sl3)
    l3 = list(l3Set)
    l3 = [list(x) for x in l3]

    return l3
