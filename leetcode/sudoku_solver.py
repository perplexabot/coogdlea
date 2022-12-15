"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""
from valid_sudoku import Solution as validator
import random


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        from itertools import product

        nd_color_map = defaultdict(set)
        adjacency_list = defaultdict(set)
        hints = []
        adjacent_color_cnt = {nd: 0 for nd in product(range(9), repeat=2)}

        def get_elem(tup):
            return board[tup[0]][tup[1]]

        def set_elem(tup, val):
            board[tup[0]][tup[1]] = str(val)

        # create adjacency_list
        for row_ind in range(9):
            for col_ind in range(9):
                col_adjs = [(row_ind, col) for col in range(9)]
                row_adjs = [(row, col_ind) for row in range(9)]
                blk_top_left = (row_ind // 3 * 3, col_ind // 3 * 3)
                blk_adjs = [
                    (blk_top_left[0] + offset[0], blk_top_left[1] + offset[1])
                    for offset in product(range(3), repeat=2)
                ]
                adjacency_list[(row_ind, col_ind)].update(col_adjs + row_adjs + blk_adjs)
                adjacency_list[(row_ind, col_ind)].discard((row_ind, col_ind))

        def get_max_adj_nds(nd_list, colored=True):
            max_nodes = []
            max_cnt = -1
            for nd in nd_list:
                edge_cnt = (
                    adjacent_color_cnt[nd]
                    if colored
                    else len(adjacency_list[nd]) - adjacent_color_cnt[nd]
                )
                if edge_cnt > max_cnt:
                    max_nodes = [nd]
                    max_cnt = edge_cnt
                elif edge_cnt == max_cnt:
                    max_nodes.append(nd)
            return max_nodes

        # initialize hint list
        for nd in product(range(9), repeat=2):
            if get_elem(nd) != '.':
                hints.append(nd)

        # create nd_color_map
        for nd in adjacency_list:
            if get_elem(nd) == '.':
                nd_color_map[nd] = set(range(1, 10))
            else:
                nd_color_map[nd] = set([int(get_elem(nd))])

        completed = set(hints)
        while all(len(nd_color_map[key]) != 1 for key in nd_color_map):
            while hints:
                nd = hints.pop()
                for adj_nd in adjacency_list[nd]:
                    adjacent_color_cnt[adj_nd] += 1
                    nd_color_map[adj_nd].discard(list(nd_color_map[nd])[0])
                    if len(nd_color_map[adj_nd]) == 1 and adj_nd not in completed:
                        hints.append(adj_nd)
                        completed.add(adj_nd)

            nd_list = set(product(range(9), repeat=2)).difference(set(completed))
            max_adj_nds = get_max_adj_nds(nd_list, colored=True)
            max_adj_nds = get_max_adj_nds(max_adj_nds, colored=False)
            hints = []
            if max_adj_nds:
                ind = random.randint(0, len(max_adj_nds) - 1)
                ind = 0
                nd_color_map[max_adj_nds[ind]] = set([min(nd_color_map[max_adj_nds[ind]])])
                hints.append(max_adj_nds[ind])
                completed.add(max_adj_nds[ind])

            print("nd_color_map: ")
            for key in nd_color_map:
                print(f"{key}: {nd_color_map[key]}")

        for nd in nd_color_map:
            set_elem(nd, nd_color_map[nd].pop())


sol = Solution()
val = validator()
boards = [
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],
    [
        [".", ".", ".", ".", ".", ".", ".", "8", "5"],
        [".", ".", ".", "2", "1", ".", ".", ".", "9"],
        ["9", "6", ".", ".", "8", ".", "1", ".", "."],
        ["5", ".", ".", "8", ".", ".", ".", "1", "6"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["8", "9", ".", ".", ".", "6", ".", ".", "7"],
        [".", ".", "9", ".", "7", ".", ".", "5", "2"],
        ["3", ".", ".", ".", "5", "4", ".", ".", "."],
        ["4", "8", ".", ".", ".", ".", ".", ".", "."],
    ],
    [
        ["9", ".", "3", ".", ".", ".", ".", "2", "4"],
        [".", ".", "7", ".", "9", "4", ".", ".", "."],
        [".", ".", "1", ".", ".", "6", ".", "3", "."],
        [".", "6", "4", ".", ".", "8", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "4", "."],
        [".", ".", ".", "9", ".", ".", ".", "5", "."],
        [".", ".", ".", ".", ".", "3", "7", ".", "."],
        ["5", ".", ".", ".", ".", ".", "1", ".", "."],
        [".", "8", ".", ".", "6", ".", ".", ".", "."],
    ],
    [
        [".", ".", ".", "7", ".", ".", "8", ".", "."],
        [".", ".", "6", ".", ".", ".", ".", "3", "1"],
        [".", "4", ".", ".", ".", "2", ".", ".", "."],
        [".", "2", "4", ".", "7", ".", ".", ".", "."],
        [".", "1", ".", ".", "3", ".", ".", "8", "."],
        [".", ".", ".", ".", "6", ".", "2", "9", "."],
        [".", ".", ".", "8", ".", ".", ".", "7", "."],
        ["8", "6", ".", ".", ".", ".", "5", ".", "."],
        [".", ".", "2", ".", ".", "6", ".", ".", "."],
    ],
    [
        ["7", "9", ".", ".", ".", ".", ".", ".", "3"],
        [".", ".", ".", ".", ".", ".", ".", "6", "."],
        ["8", ".", "1", ".", ".", "4", ".", ".", "2"],
        [".", ".", "5", ".", ".", ".", ".", ".", "."],
        ["3", ".", ".", "1", ".", ".", ".", ".", "."],
        [".", "4", ".", ".", ".", "6", "2", ".", "9"],
        ["2", ".", ".", ".", "3", ".", ".", ".", "6"],
        [".", "3", ".", "6", ".", "5", "4", "2", "1"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ],
    [
        [".", ".", "1", "3", ".", ".", "7", ".", "2"],
        [".", ".", "6", "2", ".", ".", ".", "1", "."],
        [".", "2", ".", ".", ".", ".", ".", ".", "4"],
        ["2", ".", ".", "6", ".", "1", "3", ".", "9"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["4", ".", "3", "8", ".", "9", ".", ".", "7"],
        ["1", ".", ".", ".", ".", ".", ".", "8", "."],
        [".", "5", ".", ".", ".", "6", "4", ".", "."],
        ["9", ".", "4", ".", ".", "8", "5", ".", "."],
    ],
    [
        [".", ".", ".", ".", "6", ".", ".", ".", "5"],
        ["6", "2", "4", ".", ".", ".", ".", "1", "."],
        [".", ".", "1", ".", ".", ".", "3", ".", "."],
        [".", ".", "8", ".", ".", "4", ".", "3", "7"],
        [".", ".", "9", "1", ".", ".", "5", ".", "."],
        [".", ".", "7", "5", ".", ".", ".", "9", "."],
        [".", "8", "2", "4", "7", ".", ".", ".", "."],
        [".", "9", ".", "3", "1", ".", ".", ".", "."],
        [".", ".", ".", ".", "2", "9", ".", "5", "3"],
    ],
    [
        [".", ".", ".", ".", "5", "4", "3", ".", "6"],
        [".", ".", ".", ".", ".", "3", "2", "7", "."],
        [".", ".", ".", "7", "2", ".", ".", ".", "1"],
        ["9", ".", ".", ".", "7", ".", ".", "5", "3"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["8", "2", ".", ".", "1", ".", ".", ".", "9"],
        ["3", ".", ".", ".", "6", "1", ".", ".", "."],
        [".", "4", "6", "9", ".", ".", ".", ".", "."],
        ["7", ".", "1", "5", "4", ".", ".", ".", "."],
    ],
    [
        [".", ".", "2", ".", ".", ".", "5", ".", "."],
        [".", "1", ".", "7", ".", "5", ".", "2", "."],
        ["4", ".", ".", ".", "9", ".", ".", ".", "7"],
        [".", "4", "9", ".", ".", ".", "7", "3", "."],
        ["8", ".", "1", ".", "3", ".", "4", ".", "9"],
        [".", "3", "6", ".", ".", ".", "2", "1", "."],
        ["2", ".", ".", ".", "8", ".", ".", ".", "4"],
        [".", "8", ".", "9", ".", "2", ".", "6", "."],
        [".", ".", "7", ".", ".", ".", "8", ".", "."],
    ],
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],
]

for ind, board in enumerate(boards):
    print(f"Solving board {ind}")
    sol.solveSudoku(board)
    print(f"Solved.")
    ans = val.isValidSudoku(board)
    print("Validating...")
    print("Final board: ")
    for row in board:
        print(row)
    assert ans is True
    print("A board was successfully solved")
    print("=================================================================")
