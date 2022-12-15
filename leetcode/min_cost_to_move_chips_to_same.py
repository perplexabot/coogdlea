"""We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of
    the ith chip from position[i] to:

    position[i] + 2 or position[i] - 2 with cost = 0.
    position[i] + 1 or position[i] - 1 with cost = 1.

Return the minimum cost needed to move all the chips to the same position.

Example 1:
    Input: position = [1,2,3]
    Output: 1
    Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
    Second step: Move the chip at position 2 to position 1 with cost = 1.
    Total cost is 1.

Example 2:
    Input: position = [2,2,2,3,3]
    Output: 2
    Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.

Example 3:
    Input: position = [1,1000000000]
    Output: 1

Constraints:
    1 <= position.length <= 100
    1 <= position[i] <= 10^9

    A
        0 or 1 chip(s) -> 0
    D
        [2,2,2,3,3]
        chip 0 is set to main (chip 0 is at location 2)
        chip 1 is already on main (chip 1 is at location 2)
            |2 - main| = 0 which is even so cost += 0
        chip 2 is already on main (chip 2 is at location 2)
            |2 - main| = 0 which is even so cost += 0
        chip 3 is not on main (chip 3 is at location 3)
            |3 - main| = 1 which is odd so cost += 1
        chip 4 is not on main (chip 4 is at location 3)
            |3 - main| = 1 which is odd so cost += 1
        total cost = 0 + 0 + 1 + 1 = 2
    P
        if len(position) < 2:
            return 0

        main_pos = position[0]
        for chip_pos in position[1:]:
            if abs(chip_pos - main_pos) % 2:
                cost += 1
"""


class Solution:
    def minCostToMoveChips(self, position: 'list[int]') -> int:
        from collections import Counter

        if position:
            c = Counter(position)
            main_pos = max(c, key=lambda x: c[x])
            print(f'main pos set to: {main_pos}')

        return sum(abs(main_pos - x) % 2 for x in position) if len(position) > 1 else 0


inps = [
    ([1, 2, 3], 1),
    ([2, 2, 2, 3, 3], 2),
    ([1, 1000000000], 1),
    ([2, 3, 3], 1),
    ([1], 0),
    ([], 0),
    ([1, 1], 0),
    ([1, 2], 1),
    ([6, 4, 7, 8, 2, 10, 2, 7, 9, 7], 4),
]


sol = Solution()
for inp, exp in inps:
    assert (
        ans := sol.minCostToMoveChips(inp)
    ) == exp, f"[!] Expecting {exp}, but got {ans} for the input {inp}"
