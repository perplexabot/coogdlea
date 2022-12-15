"""You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing each of them is
that adjacent houses have security system connected and it will automatically contact the
police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine
the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        sum_list = set()

        def dfs(visited, adjacents, curr_sum):
            if len(visited) + len(adjacents) >= len(nums):
                sum_list.add(curr_sum)
                return

            for i in range(len(nums)):
                if i in visited or i in adjacents:
                    continue

                t_visited = set(visited)
                t_adjacents = set(adjacents)

                t_visited.add(i)
                t_adjacents.add(i - 1)
                t_adjacents.add(i + 1)

                dfs(t_visited, t_adjacents, curr_sum + nums[i])

        dfs(set([0]), set([1]), nums[0])
        dfs(set([1]), set([0, 2]), nums[1])
        return max(sum_list)


inps = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2, 1, 1, 2], 4),
    ([], 0),
    ([1], 1),
    ([1, 100], 100),
    ([1, 2, 3], 4),
    ([1, 100, 3], 100),
]

sol = Solution()
for l, exp in inps:
    print(f"Robbing {l} (expecting {exp}) and asserting...")
    ans = sol.rob(l)
    assert ans == exp
