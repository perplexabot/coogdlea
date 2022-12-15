"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the
values in B are the same.

If it cannot be done, return -1.

Example 1:
    Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
    Output: 2
    Explanation:
        The first figure represents the dominoes as given by A and B: before we do any rotations.
        If we rotate the second and fourth dominoes, we can make every value in the top row equal
            to 2, as indicated by the second figure.
Example 2:
    Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
    Output: -1
    Explanation:
        In this case, it is not possible to rotate the dominoes to make one row of values equal.

URL: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
START: 17:40

A:
    What happens if len(A) != len(B)
    How to know if return -1

D:
    copy book

P:
    generate new sets
    a = intersect(sets)
    if not a:
        return -1

    b = a.pop()
    
    return len(A) - A.cnt(b) if A.cnt(b) > B.cnt(b) else len(B) - B.cnt(b)
"""


class Solution:
    def minDominoRotations(self, A: list[int], B: list[int]) -> int:
        if not A:
            return 0

        sets = [set(x) for x in zip(A, B)]
        common = set.intersection(*sets)

        if not common:
            return 0 if A == B else -1

        x = common.pop()
        return len(A) - A.count(x) if A.count(x) > B.count(x) else len(B) - B.count(x)


inps = [
    ([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2], 2),
    ([3, 5, 1, 2, 3], [3, 6, 3, 3, 4], -1),
    ([], [], 0),
    ([1, 1], [1, 1], 0),
    ([1, 2], [1, 2], 0),
    ([1, 2], [2, 1], 1),
]

sol = Solution()
for A, B, exp in inps:
    print(f'doing: {A}')
    assert (
        ans := sol.minDominoRotations(A, B)
    ) == exp, f"fucked up [{A}-{B}], expecting {exp}, got {ans}"
