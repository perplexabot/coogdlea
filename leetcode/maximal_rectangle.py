"""Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only
1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""


class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        from itertools import groupby

        if not matrix:
            return 0

        if len(matrix) == 1:
            if not matrix[0]:
                return 0
            g = groupby(matrix[0])
            return max([len(list(y)) for x, y in g if x == '1'], default=0)

        link = [''.join(row) for row in matrix]
        cnt = 1
        areas = []
        while link:
            prev = int(link[0], base=2)
            newL = []

            for row in link:
                g = groupby(row)
                l = [len(list(y)) * cnt for x, y in g if x == '1']
                areas.extend(l)

            j = 1
            while j < len(link):
                intj = int(link[j], base=2)
                newL.append('{0:b}'.format(prev & intj))
                prev = intj
                j += 1

            cnt += 1
            link = newL
        return max(areas, default=0)


inps = [
    (
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        6,
    ),
    ([], 0),
    (None, 0),
    ([[]], 0),
    ([['0']], 0),
    ([['1'], ['1'], ['1']], 3),
    ([['1'], ['1'], ['0'], ['1']], 2),
    (
        [
            ['0', '0', '0', '0', '0', '0', '0'],
            ['1', '1', '0', '1', '1', '0', '0'],
            ['1', '1', '0', '0', '1', '0', '1'],
            ['0', '1', '0', '0', '1', '0', '1'],
            ['0', '1', '1', '0', '0', '0', '0'],
            ['0', '1', '1', '0', '0', '0', '0'],
        ],
        5,
    ),
    ([['0', '0'], ['0', '0']], 0),
    ([['1', '0'], ['0', '1']], 1),
]

sol = Solution()
for inp, exp in inps:
    print(f"Finding max area of ones for {inp} and asserting...")
    ans = sol.maximalRectangle(inp)
    print(f" got: {ans}, exp: {exp}")
    assert exp == ans
