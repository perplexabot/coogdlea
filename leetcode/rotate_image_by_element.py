"""You are given an n x n 2D matrix representing an image.

Rotate the image by 1 element (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        def get_loops(n):
            i = n
            loops = []
            while i > 0:
                j = n - i
                if n - (j * 2) < 2:
                    if n % 2:
                        loops.append([(n // 2, n // 2)])
                    break

                loop = []
                # top
                for x in range(j, i):
                    loop.extend([(j, x)])

                # right
                for x in range(j + 1, i - 1):
                    loop.extend([(x, i - 1)])

                # bottom
                temp = []
                for x in range(j, i):
                    temp.extend([(i - 1, x)])
                loop.extend(temp[::-1])

                # left
                temp = []
                for x in range(j + 1, i - 1):
                    temp.extend([(x, j)])
                loop.extend(temp[::-1])

                loops.append(loop)
                i -= 1
            return loops

        def rotate_loop(loop_locations, ind, matrix, init):
            curr_element_location = loop_locations[ind]
            row = curr_element_location[0]
            col = curr_element_location[1]
            new_init = matrix[row][col]
            matrix[row][col] = init
            if ind < len(loop_locations) - 1:
                rotate_loop(loop_locations, ind + 1, matrix, new_init)

        n = len(matrix)
        loops = get_loops(n)

        for loop in loops:
            rotate_loop(loop, 0, matrix, matrix[loop[-1][0]][loop[-1][1]])


sol = Solution()
matrices = [
    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
]


def printMatrix(mat):
    for row in mat:
        print(row)


for mat in matrices:
    print("Before: ")
    printMatrix(mat)
    sol.rotate(mat)
    print("After: ")
    printMatrix(mat)
    print("------------------------------------")
