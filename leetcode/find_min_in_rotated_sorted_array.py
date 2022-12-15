"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        def binaryFind(s, e):
            if e - s == 1:
                if nums[e] < nums[s]:
                    return nums[e]
                else:
                    return None

            if not e - s:
                return None

            piv = (e - s) // 2 + s
            pivl = (piv - s) // 2 + s
            pivr = e - (e - piv) // 2

            if nums[pivl] > nums[piv]:
                return binaryFind(pivl, piv)
            elif nums[pivr] < nums[piv]:
                return binaryFind(piv, pivr)
            else:
                ans = binaryFind(s, pivl)
                return ans if ans is not None else binaryFind(pivr, e)

        return binaryFind(0, len(nums) - 1)


from random import randint

random_vecs = []
for i in range(1000):
    size = randint(0, 50)

    random_vec = list(set([randint(-100, 100) for _ in range(size + 1)]))
    random_vec.sort()
    m = random_vec[0]
    rot_pt = randint(0, len(random_vec))

    random_vec = random_vec[rot_pt:] + random_vec[:rot_pt]
    random_vecs.append((random_vec, m))

inps = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([1], 1),
    ([2, 1], 1),
    ([1, 2], 1),
    ([3, 1, 2], 1),
    ([9, 1, 2, 3, 4, 5, 6, 7, 8], 1),
    ([-6, 37, 63, -77], -77),
]

inps.extend(random_vecs)

sol = Solution()
for nums, exp in inps:
    print(f"Finding min in rotated list '{nums}' and asserting...")
    assert sol.findMin(nums) == exp
