"""The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two
queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
both indicate a queen and an empty space respectively.

Example:
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        def q_locs_to_board(qlocs):
            board = [['.'] * n for _ in range(n)]
            for qloc in qlocs:
                board[qloc[0]][qloc[1]] = 'Q'
            return [''.join(row) for row in board]

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

        solutions = []

        def nQSolver(col_ind, bad_cells, Q_locs):
            for row_ind in range(n):
                if (col_ind, row_ind) not in bad_cells:
                    Q_locs.add((col_ind, row_ind))
                    if len(Q_locs) == n:
                        solutions.append(Q_locs)
                        return
                    old_bad_cells = set(bad_cells)
                    bad_cells.update(associated_cells[(col_ind, row_ind)])
                    nQSolver(col_ind + 1, bad_cells, set(Q_locs))
                    bad_cells = old_bad_cells
                    Q_locs.remove((col_ind, row_ind))

        associated_cells = defaultdict(set)
        init_association_dict(associated_cells)
        nQSolver(0, set(), set())
        boards = []
        for qlocs in solutions:
            boards.append(q_locs_to_board(qlocs))
        return boards


import pprint

sol = Solution()
for i in range(7):
    print(f"Doing {i}...")
    ans = sol.solveNQueens(i)
    pprint.pprint(ans)
