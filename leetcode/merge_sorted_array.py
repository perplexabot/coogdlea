"""Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:]
        place, i, j = 0, 0, 0
        while i < m and j < n:
            if tmp[i] < nums2[j]:
                nums1[place] = tmp[i]
                i += 1
            else:
                nums1[place] = nums2[j]
                j += 1
            place += 1

        while i < m:
            nums1[place] = tmp[i]
            i += 1
            place += 1

        while j < n:
            nums1[place] = nums2[j]
            j += 1
            place += 1


sol = Solution()
inps = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
    ([1, 3, 5, 0, 0, 0], 3, [0, 2, 4], 3),
    ([1, 3, 5, 0, 0, 0], 3, [6, 7, 8], 3),
    ([1, 0], 1, [2], 1),
    ([1, 0], 1, [-1], 1),
    ([1], 1, [], 0),
    ([0], 0, [1], 1),
    ([1, 2, 3, 0, 0, 0], 3, [-3, -2, -1], 3),
    ([-3, -2, -1, 0, 0, 0], 3, [1, 2, 3], 3),
    ([1, 2, 3, 5, 6, 7, 8, 0], 7, [4], 1),
]

for inp in inps:
    sol.merge(*inp)
    print(f'final ans: {inp[0]}')
