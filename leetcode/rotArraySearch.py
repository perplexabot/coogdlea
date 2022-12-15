"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
import random


class Solution(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    def find_rotation(self, lst, start, end):
        if start == end:
            return 0

        piv = start + ((end-start)//2)
        piv_l = start + ((piv-start)//2)
        piv_r = piv + ((end-piv)//2 + 1)

        if lst[piv_l] > lst[piv]:
            if piv-piv_l == 1:
                return piv
            return self.find_rotation(lst, piv_l, piv)
        if lst[piv_r] < lst[piv]:
            if piv_r-piv == 1:
                return piv_r
            return self.find_rotation(lst, piv, piv_r)

        ans_l = self.find_rotation(lst, start, piv_l)
        ans_r = self.find_rotation(lst, piv_r, end)
        if ans_l != 0:
            return ans_l
        if ans_r != 0:
            return ans_r
        return 0

    # start and end are valid indices that have already rotated as needed
    def bin_search(self, start, end, tgt, lst, offset=0):
        if start > end:
            return -1
        piv = start + (end-start)//2

        # rotated points
        rot_piv = (piv + offset) % len(lst)

        if lst[rot_piv] == tgt:
            return rot_piv
        elif tgt < lst[rot_piv]:
            return self.bin_search(start, piv-1, tgt, lst, offset=offset)
        return self.bin_search(piv+1, end, tgt, lst, offset=offset)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        offset = self.find_rotation(nums, 0, len(nums)-1)
        return self.bin_search(0, len(nums)-1, target, nums, offset=offset)


# Testing find_rotation()
print("=========================================================")
print(" Testing find_rotation()")
print("=========================================================")
sol = Solution()
TEST_COUNT = 10
for i in range(TEST_COUNT):
    LIST_SIZE = random.randint(1, 10)
    rand_arr = [random.randint(-100, 100) for _ in range(LIST_SIZE)]
    rand_arr.sort()
    first_elem = rand_arr[0]
    rot_pt = random.randint(1, max(LIST_SIZE-2, 1))
    rota_arr = rand_arr[rot_pt:] + rand_arr[:rot_pt]
    print("org list: ", rand_arr)
    print(" rot list: ", rota_arr)
    rot = sol.find_rotation(rota_arr, 0, len(rota_arr)-1)
    print(" rotation: ", rot)
    assert rota_arr[rot] == first_elem
    print("PASSED")

print("=========================================================")
print(" Testing bin_search()")
print("=========================================================")
# Testing bin_search
TEST_COUNT = 10
for i in range(TEST_COUNT):
    LIST_SIZE = random.randint(1, 10)
    rand_arr = [random.randint(-100, 100) for _ in range(LIST_SIZE)]
    target = rand_arr[LIST_SIZE//2]
    rand_arr.sort()
    rot_pt = random.randint(1, max(LIST_SIZE-2, 1))
    rota_arr = rand_arr[rot_pt:] + rand_arr[:rot_pt]
    print("org list: ", rand_arr)
    print(" rot list: ", rota_arr)
    print(" target  : ", target)
    offset = sol.find_rotation(rota_arr, 0, len(rota_arr)-1)
    print(" offset: ", offset)
    ans = sol.bin_search(0, len(rota_arr)-1, target, rota_arr, offset)
    print(" bin_search: ", ans)
    assert ans == rota_arr.index(target)
    print("PASSED!")

print("=========================================================")
print(" Testing search()")
print("=========================================================")
# Testing bin_search
TEST_COUNT = 10
for i in range(TEST_COUNT):
    LIST_SIZE = random.randint(1, 10)
    rand_arr = [random.randint(-100, 100) for _ in range(LIST_SIZE)]
    target = rand_arr[LIST_SIZE//2]
    rand_arr.sort()
    rot_pt = random.randint(1, max(LIST_SIZE-2, 1))
    rota_arr = rand_arr[rot_pt:] + rand_arr[:rot_pt]
    print("org list: ", rand_arr)
    print(" rot list: ", rota_arr)
    print(" target  : ", target)
    ans = sol.search(rota_arr, target)
    print(" found index: ", ans)
    assert ans == rota_arr.index(target)
    print("PASSED!")
