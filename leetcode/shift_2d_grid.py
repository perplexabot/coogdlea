"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
In one shift operation:
    Element at grid[i][j] moves to grid[i][j + 1].
    Element at grid[i][n - 1] moves to grid[i + 1][0].
    Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m <= 50
    1 <= n <= 50
    -1000 <= grid[i][j] <= 1000
    0 <= k <= 100

A:
    if 2d is a 1d vector    ->  return reverse of vector
    if 2d is empty          ->  return itself
    if m != n               ->  who cares

D:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
        1 2 3
        4 5 6
        7 8 9

    row = 0
        r0_last = row[0][end]
        row[0][1] = row[0][1-1]
        row[0][2] = row[0][2-1]
    row = 1
        r1_last = row[1][end]
        row[1][1] = row[1][1-1]
        row[1][2] = row[1][2-1]
        row[1][0] = r0_last
    row = 2
        r2_last = row[2][end]
        row[2][1] = row[2][1-1]
        row[2][2] = row[2][2-1]
        row[2][0] = r1_last

    row[0][0] = r2_last

    if k > 1, do above k times

P:
    if grid empty   ->  return empty
    if grid is 1d array ->  shift

    end_values = [row[-1] for row in grid]
    m = len(grid)
    n = len(grid[0])

    for row_index in range(m):
        for col_index in range(1,n):
            grid[row_index][col_index] = grid[row_index][col_index-1]
        grid[row_index][-1] = end_values[-1 - row_index]

"""


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0]) if type(grid[0]) is list else 1

        if m == n == 1:
            return grid

        # this if can be optimized a lot but I need to walk the dog...
        if m == 1:
            inside = grid[0]
            for i in range(k):
                inside = [inside[-1]] + inside[:-1]
            return [inside]
        if n == 1:
            for i in range(k):
                grid = [grid[-1]] + grid[:-1]
            return grid

        for i in range(k):
            end_values = [row[-1] for row in grid]
            for row_index in range(m):
                curr_row = grid[row_index][:]
                for col_index in range(1, n):
                    grid[row_index][col_index] = curr_row[col_index - 1]

                grid[row_index][0] = end_values[row_index - 1]
 
        return grid


cases = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [[9, 1, 2], [3, 4, 5], [6, 7, 8]]),
    (
        [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
        4,
        [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]],
    ),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ([[1], [2], [3]], 1, [[3], [1], [2]]),
    ([1, 2, 3], 1, [3, 1, 2]),
    ([[1], [2], [3], [4], [7], [6], [5]], 23, [[6], [5], [1], [2], [3], [4], [7]]),
    ([[1]], 100, [[1]]),
    (
        [
            [
                215,
                -322,
                -930,
                -619,
                334,
                367,
                -381,
                -629,
                731,
                197,
                -340,
                333,
                -150,
                899,
                683,
                405,
                461,
                -104,
                -556,
                301,
                962,
                286,
                418,
                236,
                657,
                -27,
                -287,
                -410,
                -931,
            ]
        ],
        1,
        [
            [
                -931,
                215,
                -322,
                -930,
                -619,
                334,
                367,
                -381,
                -629,
                731,
                197,
                -340,
                333,
                -150,
                899,
                683,
                405,
                461,
                -104,
                -556,
                301,
                962,
                286,
                418,
                236,
                657,
                -27,
                -287,
                -410,
            ]
        ],
    ),
]

sol = Solution()
for (grid, k, exp) in cases:
    assert (
        got := sol.shiftGrid(grid, k)
    ) == exp, f"Failed case ({grid}, {k}) - expecting ({exp}), got ({got})."
