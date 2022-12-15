"""Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import Counter

        def dfs(candidates, tgt, combo, combos, curr_cnt, last):
            if tgt == 0:
                combos.append(combo)
                return
            if tgt < candidates[0]:
                return

            for candidate in candidates:
                if candidate > tgt:
                    break
                if curr_cnt[candidate] >= total_cnts[candidate] or candidate < last:
                    continue
                updated_cnt = dict(curr_cnt)
                updated_cnt[candidate] += 1
                dfs(
                    candidates, tgt - candidate, combo + [candidate], combos, updated_cnt, candidate
                )

        combos = []
        total_cnts = Counter(candidates)
        candidates = sorted(set(candidates))
        curr_cnts = {x: 0 for x in candidates}
        dfs(candidates, target, [], combos, curr_cnts, 0)
        return combos


sol = Solution()
candidates = [[10, 1, 2, 7, 6, 1, 5], [2, 5, 2, 1, 2]]
targets = [8, 5]
for target, candidate in zip(targets, candidates):
    print("Candy list: ", candidate)
    print(" target: ", target)
    ans = sol.combinationSum2(candidate, target)
    print(" ans: ", ans)
