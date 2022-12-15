"""Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral
order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        output = []
        m = len(matrix)  # rows
        n = len(matrix[0])  # cols
        curr_loop_dim = [m, n]

        def getLoopElementsClockWise(loop_index):
            output = []

            # top (left to right)
            output.extend([matrix[loop_index][x] for x in range(loop_index, n - loop_index - 1)])

            # right (top to bottom)
            output.extend(
                [matrix[x][n - 1 - loop_index] for x in range(loop_index, m - loop_index - 1)]
            )

            # bottom (right to left)
            output.extend(
                [
                    matrix[m - 1 - loop_index][x]
                    for x in reversed(range(loop_index + 1, n - loop_index))
                ]
            )

            # left (bottom to top)
            output.extend(
                [matrix[x][loop_index] for x in reversed(range(loop_index + 1, m - loop_index))]
            )
            return output

        loop_ind = 0
        while 1 not in curr_loop_dim and len(output) < n * m:
            output.extend(getLoopElementsClockWise(loop_ind))
            curr_loop_dim = [x - 2 for x in curr_loop_dim]
            loop_ind += 1

        if 1 in curr_loop_dim and len(output) != n * m:
            if curr_loop_dim[0] == 1:
                output.extend([matrix[m // 2][x] for x in range(loop_ind, n - loop_ind)])
            else:
                output.extend([matrix[x][n // 2] for x in range(loop_ind, m - loop_ind)])
        return output


sol = Solution()
inp = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    [[3], [2]],
    [[2, 5, 8], [4, 0, -1]],
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
        [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
        [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
        [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
        [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
        [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
    ],
]
for mat in inp:
    print("Spiraling: ", mat)
    ans = sol.spiralOrder(mat)
    print(" ans: ", ans)
