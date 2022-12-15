# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def partition(st, en, lst):
            i = st-1
            j = en+1
            p = st

            while True:
                i+=1
                while lst[i] < lst[p]:
                    i += 1
                j-=1
                while lst[j] > lst[p]:
                    j -= 1

                if i >= j:
                    return j

                lst[i], lst[j] = lst[j], lst[i]

        def quickSort(st,en,lst):
            if st < en:
                p = partition( st, en, lst )
                quickSort( st, p, lst )
                quickSort( p+1, en, lst )

        def getClosestFromBelow(lst, startIndex, c):
            mx = lst[startIndex]
            ind = startIndex
            for i in range(startIndex, len(lst)):
                if lst[i] < mx and lst[i] > c:
                    mx = lst[i]
                    ind = i
            return ind 
        
        j = len(nums) - 2
        while j > 0 and nums[j] >= nums[j+1]:
            j -= 1
        
        if len(nums) < 2:
            return
        elif nums[j] < nums[j+1]:
            # by design (usage of getMaxIndex), getMaxIndex will never return None
            maxInd = getClosestFromBelow(nums, j+1, nums[j])
            nums[j], nums[ maxInd ] = nums[ maxInd ], nums[j]
            print('about to sort: ', nums[j+1: len(nums)] )
            quickSort( j+1, len(nums)-1, nums)
            print('sorted to: ', nums[j+1: len(nums) ] )
        else:
            nums.sort()

s = Solution()

l = [12,5,3,9,2,1]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = [1,2,3]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = [3,2,1]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = [1,1,5]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = []
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = [1]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = [2,1]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = [1,1,1]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = [1,2]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = [1,3,2]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
print('================')

l = [2,2,7,5,4,3,2,2,1]
print("lo: ", l)
s.nextPermutation(l)
print("ln: ", l)
