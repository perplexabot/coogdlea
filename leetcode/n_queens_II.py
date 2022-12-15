"""The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other. Given an integer n, return the
number of distinct solutions to the n-queens puzzle.

Example:
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import defaultdict

        def init_association_dict(associated_cells):
            for col in range(n):
                for row in range(n):
                    cell = (col, row)
                    for i in range(n):
                        associated_cells[(i, row)].add(cell)
                    for i in range(n):
                        associated_cells[(col, i)].add(cell)

                    offset = min(cell)
                    x, y = cell[0] - offset, cell[1] - offset
                    while all([x < n, y < n]):
                        associated_cells[(x, y)].add(cell)
                        x += 1
                        y += 1

                    x_inter = sum(cell)
                    x, y = (n, -n + x_inter) if x_inter > n else (x_inter, 0)
                    while all([x > -1, y < n]):
                        associated_cells[(x, y)].add(cell)
                        x -= 1
                        y += 1

        def nQSolver(col_ind, bad_cells, q_cnt, sol_cnt):
            for row_ind in range(n):
                if (col_ind, row_ind) not in bad_cells:
                    q_cnt += 1
                    if q_cnt == n:
                        sol_cnt[0] += 1
                        return
                    old_bad_cells = set(bad_cells)
                    bad_cells.update(associated_cells[(col_ind, row_ind)])
                    nQSolver(col_ind + 1, bad_cells, q_cnt, sol_cnt)
                    bad_cells = old_bad_cells
                    q_cnt -= 1

        sol_cnt = [0]
        associated_cells = defaultdict(set)
        init_association_dict(associated_cells)
        nQSolver(0, set(), 0, sol_cnt)
        return sol_cnt[0]


import pprint

sol = Solution()
for i in range(10):
    print(f"doing {i}")
    ans = sol.totalNQueens(i)
    print(f" got {ans}")
