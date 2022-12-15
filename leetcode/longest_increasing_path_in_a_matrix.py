"""Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT
move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


class Solution:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> 'int':
        def isValid(src):
            if src[0] < 0 or src[0] >= m:
                return False
            if src[1] < 0 or src[1] >= n:
                return False
            return True

        def get_neighbors(src):
            row = src[0]
            col = src[1]
            n = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            return [neigh for neigh in n if isValid(neigh)]

        memo = {}

        def path_to_memo(path, offset=0):
            pLen = len(path)
            for ind, src in enumerate(path):
                if src not in memo:
                    memo[src] = (pLen - ind) + offset
                else:
                    if memo[src] < (pLen - ind) + offset:
                        memo[src] = (pLen - ind) + offset

        def dfs(src, prev_val, path, i):
            if matrix[src[0]][src[1]] <= prev_val:
                path_to_memo(path)
                usedSrcs.update(path)
            else:
                path.append(src)
                for n in get_neighbors(src):
                    if n in memo and matrix[src[0]][src[1]] < matrix[n[0]][n[1]]:
                        path_to_memo(path, offset=memo[n])
                        usedSrcs.update(path)
                    else:
                        dfs(n, matrix[src[0]][src[1]], path[:], i + 1)

        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        if not n:
            return 0

        usedSrcs = set()
        ini_prev = float('-inf')

        for i in range(m):
            for j in range(n):
                if (i, j) in usedSrcs:
                    continue
                dfs((i, j), ini_prev, [], 0)

        return max(memo.values(), default=1)


inps = [
    ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
    ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
    ([[1]], 1),
    ([[1], [2]], 2),
    ([[1, 2, 3, 4, 5]], 5),
    ([[5, 4, 3, 2, 1]], 5),
    ([[5], [4], [3], [2], [1]], 5),
    ([[1], [2], [3], [4], [5]], 5),
    (
        [
            [-20, 6, 17, -4, -5],
            [11, -13, 20, 15, -9],
            [15, 9, 18, 8, -17],
            [-16, -19, 7, -14, -5],
            [-14, 11, 16, -3, 2],
        ],
        6,
    ),
    (
        [
            [1, 11, 0, 20, -14, 17, -17],
            [-16, 5, -4, 3, 4, -1, 13],
            [12, -16, 12, 11, 18, -16, 18],
            [-3, -11, -9, 4, -18, 7, 19],
        ],
        6,
    ),
    ([], 0),
    ([[]], 0),
    (
        [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
            [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
            [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
            [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
            [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
            [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
            [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
            [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
            [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
            [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
            [119, 118, 117, 116, 115, 114, 113, 112, 111, 110],
            [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
            [139, 138, 137, 136, 135, 134, 133, 132, 131, 130],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
        140,
    ),
]

sol = Solution()
for mat, exp in inps:
    n = len(mat)
    m = 0 if not n else len(mat[0])
    n = 0 if not m else n
    print(f"Doing {n}x{m} mat: ", mat)
    ans = sol.longestIncreasingPath(mat)
    print(f' got: {ans} expected: {exp}')
    assert ans == exp
