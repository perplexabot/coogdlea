"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and
    maximum in its column.

Example 1:
    Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
    Output: [15]
    Explanation: 15 is the only lucky number since it is the minimum in its row and the
        maximum in its column
Example 2:
    Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    Output: [12]
    Explanation: 12 is the only lucky number since it is the minimum in its row and the
        maximum in its column.
Example 3:
    Input: matrix = [[7,8],[1,2]]
    Output: [7]

URL: https://leetcode.com/problems/lucky-numbers-in-a-matrix/

A:
    Case where n = m = 1
    Case where n = 0
    Case where m = 0
    Case where n and m are 0
    Case with no lucky numbers
    Case for column matrix (vector)
    Case with no lucky numbers?
    Mind duplicates (track my index)

D:
    [[3, 7 , 8],
     [9, 11, 13],
     [15,16, 17]]

     lucky_min_indices = [(0,0), (1,0), (2,0)]
     lucky_max_indices = [(2,0), (2,1), (2,2)]
     lucky_numbers = (2,0)

P:
    lucky_min_indices = set([min(x) for x in matrix])
    lucky_max_indices = set([max(x) for x in zip(*matrix)
    return lucky_min_indices & lucky_max_indices
"""


class Solution:
    def luckyNumbers(self, matrix: 'List[List[int]]') -> 'List[int]':
        if not len(matrix):
            return []

        lucky_min_indices = set(
            min([(ir, i) for i in range(len(row))], key=lambda x: matrix[x[0]][x[1]])
            for ir, row in enumerate(matrix)
        )
        lucky_max_indices = set(
            max([(i, ic) for i in range(len(col))], key=lambda x: matrix[x[0]][x[1]])
            for ic, col in enumerate(zip(*matrix))
        )
        return [matrix[x[0]][x[1]] for x in lucky_min_indices & lucky_max_indices]


inps = [
    ([[1]], [1]),
    ([[1], [2], [3]], [3]),
    ([[1, 2, 3]], [1]),
    ([], []),
    ([[3, 7, 8], [9, 11, 13], [15, 16, 17]], [15]),
    ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], [12]),
    ([[7, 8], [1, 2]], [7]),
]

sol = Solution()
for inp, exp in inps:
    ans = sol.luckyNumbers(inp)
    assert ans == exp, f"Failed to do {str(inp)}, got: {str(ans)}, expecting: {str(exp)}"
