"""Given an unsorted array of integers, find the length of the longest consecutive elements
sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        nums = set(nums)
        v = {}
        adj_left = {}
        adj_right = {}
        for n in nums:
            if n - 1 in v and n + 1 in v:
                left = adj_left[n - 1] if adj_left[n - 1] else n - 1
                right = adj_right[n + 1] if adj_right[n + 1] else n + 1
                adj_right[left] = right
                adj_left[right] = left
                k = v[left] + v[right] + 1
                v[left] = k
                v[right] = k
            elif n - 1 in v:
                left = adj_left[n - 1] if adj_left[n - 1] else n - 1
                adj_right[left] = n
                adj_left[n] = left
                v[n] = v[left] + 1
                v[left] += 1
            elif n + 1 in v:
                right = adj_right[n + 1] if adj_right[n + 1] else n + 1
                adj_left[right] = n
                adj_right[n] = right
                v[n] = v[right] + 1
                v[right] += 1
            else:
                v[n] = 1
                adj_left[n] = None
                adj_right[n] = None
        print(v)
        return max(v.values())


inps = [
    ([1, 2], 2),
    ([1, 2, 4, 3], 4),
    ([1, 4, 2, 3], 4),
    ([1, 3, 4, 2], 4),
    ([1, 2, 4, 5, 3], 5),
    ([2, 1, 5, 4, 3], 5),
    ([100, 4, 200, 1, 3, 2], 4),
    ([1, 4, 2, 4, 3, 4, 5], 5),
    ([1, 1, 1, 1, 1, 1, 1, 1], 1),
    (None, 0),
    ([], 0),
    ([1, 2, 3, 4, 5, 6], 6),
    ([6, 5, 4, 3, 2, 1], 6),
    ([-1, 1, 2, 0], 4),
    (
        [
            -3,
            2,
            8,
            5,
            1,
            7,
            -8,
            2,
            -8,
            -4,
            -1,
            6,
            -6,
            9,
            6,
            0,
            -7,
            4,
            5,
            -4,
            8,
            2,
            0,
            -2,
            -6,
            9,
            -4,
            -1,
        ],
        7,
    ),
]

sol = Solution()
for nums, exp in inps:
    print(f"Finding longest consecutive seq in {nums} and asserting...")
    ans = sol.longestConsecutive(nums)
    assert ans == exp
print("----------")
print("  PASSED  ")
print("----------")
