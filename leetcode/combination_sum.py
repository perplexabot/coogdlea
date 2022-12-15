"""Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # to get rid of duplicates, make combos a set
        # combos takes frozensets as elements.
        # the frozensets are contain tuples that dictate
        # the integer and its count for a certain combo.
        # post process to create returnable combo list
        combo_dict = {}
        combo_dict[1] = [[1]]
        sorted_candidate_list = sorted(list(candidates))

        def getCombSet(tgt):
            if tgt < sorted_candidate_list[0]:
                return []

            if tgt in combo_dict:
                return combo_dict[tgt]

            if tgt == 1:
                return [1]

            combos = set()
            for elem in sorted_candidate_list:
                if elem > tgt:
                    break

                if elem == tgt:
                    combos.add(frozenset(Counter([tgt]).items()))
                    continue

                mult = 1
                partial_sum = elem * mult
                while partial_sum < tgt:
                    left_over_sum = tgt - partial_sum
                    if left_over_sum > elem:
                        left_over_sets = getCombSet(left_over_sum)
                        for left_over_set in left_over_sets:
                            combos.add(frozenset(Counter([elem] * mult + left_over_set).items()))
                    mult += 1
                    partial_sum = elem * mult
            combo_dict[tgt] = combos
            return combos

        return getCombSet(target)


sol = Solution()

print("USING CANDIDATES: ", [2, 3, 6, 7])
# ans = sol.combinationSum([2, 3, 6, 7], 1)
# print("1 ans: ", ans)
# print("--------------------------------")
#
# ans = sol.combinationSum([2, 3, 6, 7], 2)
# print("2 ans: ", ans)
# print("--------------------------------")
#
# ans = sol.combinationSum([2, 3, 6, 7], 5)
# print("3 ans: ", ans)
# print("--------------------------------")

ans = sol.combinationSum([2, 3, 6, 7], 7)
print("7 ans: ", ans)
print("--------------------------------")


# print("USING CANDIDATES: ", [2, 3, 5])
# ans = sol.combinationSum([2, 3, 5], 8)
# print("8 ans: ", ans)
# print("--------------------------------")
