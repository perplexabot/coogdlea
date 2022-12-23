"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the
    ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will
    have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:
    Input: candies = [2,3,5,1,3], extraCandies = 3
    Output: [true,true,true,false,true]
    Explanation: If you give all extraCandies to:
    - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
    - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
    - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
    - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Example 2:
    Input: candies = [4,2,1,1,2], extraCandies = 1
    Output: [true,false,false,false,false]
    Explanation: There is only 1 extra candy.
    Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

Example 3:
    Input: candies = [12,1,12], extraCandies = 10
    Output: [true,false,true]

Constraints:
    n == candies.length
    2 <= n <= 100
    1 <= candies[i] <= 100
    1 <= extraCandies <= 50

A:
    candies = []            ->      return []
    extraCandies = 0        ->      return [true if x in candles is max(candles)]
    negative nums in input  ->      not possible according to constraint
A:
    ?
D:
    candies = [2,3,5,1,3], extraCandies = 3
    m = max(candies) = 5
    candies[0] -> m - candies[0] = 5 - 2 = 3 <= extraCandies, True
    candies[1] -> m - candies[1] = 5 - 3 = 2 <= extraCandies, True
    candies[2] -> m - candies[2] = 5 - 5 = 0 <= extraCandies, True
    candies[3] -> m - candies[3] = 5 - 1 = 4 >  extraCandies, False
    candkes[4] -> m - candies[4] = 5 - 3 = 1 <= extraCandies, True

"""


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    if not candies:
        return []

    m = max(candies)
    if not extraCandies:
        return [x >= m for x in candies]

    return [m - ccnt <= extraCandies for ccnt in candies]


cases = [
    ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
    ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
    ([12, 1, 12], 10, [True, False, True]),
    ([], 10, []),
    ([1, 2], 0, [False, True]),
    ([2, 2], 0, [True, True]),
    ([1], 0, [True]),
    ([1], 10, [True]),
]

for (candies, extraCandies, exp) in cases:
    assert (
        got := kidsWithCandies(candies, extraCandies)
    ) == exp, f"Failed case ({candies}, {extraCandies}) - expecting ({exp}), got ({got})"
