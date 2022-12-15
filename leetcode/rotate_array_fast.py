"""Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve
this problem.
Could you do it in-place with O(1) extra space?
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        ll = len(nums)
        k = k % ll

        if not k:
            return

        start = 0
        curr = start
        v = nums[start]
        for j in range(ll):
            v, nums[curr] = nums[curr], v
            curr = (curr + k) % ll
            if curr == start:
                nums[curr] = v
                start += 1
                v = nums[start]
                curr = start


from random import randint


def fake_rot(l, k):
    k = k % len(l)
    return l[-k:] + l[:-k]


sol = Solution()
inps = [
    ([1, 2, 3, 4, 5, 6, 7], 3),
    ([-1, -100, 3, 99], 2),
    ([51, 3, 28, 8, 65, -93, -90, 59], 9),
    ([46, -53, 91, -82, -82, 75, -94, 83, 70, -66], 2),
]

min_bound = -100
max_bound = 100
list_of_test_vecs_size = 1000
test_vec_max_size = 10
list_of_test_vecs = [
    (
        [randint(min_bound, max_bound) for _ in range(randint(0, test_vec_max_size))],
        randint(0, test_vec_max_size),
    )
    for _ in range(list_of_test_vecs_size)
]

inps.extend(list_of_test_vecs)

for l, k in inps:
    print(f"About to rotate {l} by {k}")
    if l:
        t = k % len(l)
    exp = fake_rot(l, t) if t and l else l
    sol.rotate(l, k)
    print(f" GOT: {l}")
    print(f" EXP: {exp}")
    assert exp == l
