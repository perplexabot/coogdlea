"""Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(1) == len(nums):
            return len(nums) - 1

        paths = []

        def jmp_recurse(start, path):
            if not start:
                paths.append(path)
                return

            ind = 0
            while ind < start and not paths:
                if nums[ind] + ind >= start:
                    jmp_recurse(ind, path + [ind])
                ind += 1

        jmp_recurse(len(nums) - 1, [])
        return len(min(paths, key=len))


inps = [
    ([2, 3, 1, 1, 4], 2),
    ([100, 1, 1, 1, 1, 1, 1, 1, 1], 1),
    ([5, 1, 2, 3, 4, 5], 1),
    ([4, 1, 2, 3, 4, 5], 2),
    ([1, 1, 1, 1, 1, 1], 5),
    ([2, 0, 2, 0, 2], 2),
    ([0], 0),
    ([10], 0),
    ([1, 0], 1),
    ([2, 0], 1),
    ([2, 0, 3, 0, 0, 4, 0, 0, 0, 5], 3),
    ([2, 1, 3, 1, 1, 4, 1, 1, 1, 5], 3),
    (
        [
            5,
            6,
            4,
            4,
            6,
            9,
            4,
            4,
            7,
            4,
            4,
            8,
            2,
            6,
            8,
            1,
            5,
            9,
            6,
            5,
            2,
            7,
            9,
            7,
            9,
            6,
            9,
            4,
            1,
            6,
            8,
            8,
            4,
            4,
            2,
            0,
            3,
            8,
            5,
        ],
        5,
    ),
]

sol = Solution()
for inp, exp in inps:
    print(f"Doing {inp} and asserting...")
    ans = sol.jump(inp)
    assert ans == exp
print("**** PASSED! ****")
