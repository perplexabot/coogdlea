"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
    Input:
        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        target = 3
    Output: true

Example 2:
    Input:
        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        target = 13
    Output: false

URL: https://leetcode.com/problems/search-a-2d-matrix/

AADPOCT

A:
    Matrix of size 0 x 0, 1 x n, n x 1, 1 x 1
A:
    ?
D:
    target = 13
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]

    is 13 >= 23? no
    is 13 >= 10? yes
        if 13 == 10:
            return True
        binary search row for value
P:
    for row in matrix:
        if target <= row[-1]:
            return True if found in binary_search(row, target) else False
    return False
O:
    ?
"""


class Solution:
    from bisect import bisect_left as bl

    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        for row in matrix:
            if row and target <= row[-1]:
                i = self.bl(row, target)
                return i < len(row) and row[i] == target
        return False


inps = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 1, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 23, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 50, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11, True),
    ([[1, 3, 5, 7]], 1, True),
    ([[1, 3, 5, 7]], 3, True),
    ([[1, 3, 5, 7]], 7, True),
    ([[1, 3, 5, 7]], 17, False),
    ([[1], [3], [5], [7]], 1, True),
    ([[1], [3], [5], [7]], 7, True),
    ([[1], [3], [5], [7]], 3, True),
    ([[1], [3], [5], [7]], 0, False),
    ([[1], [3], [5], [7]], 100, False),
    ([[1]], 1, True),
    ([[1]], 0, False),
    ([], 0, False),
    ([[]], 0, False),
    ([[], []], 0, False),
]

sol = Solution()
for matrix, target, exp in inps:
    assert (
        ans := sol.searchMatrix(matrix, target)
    ) == exp, f"matrix: {matrix}, target: {target}, ans: {ans}, exp: {exp}"
