"""You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        def rotate_90(location, n):
            return (location[1], (n - 1) - location[0])

        def recurse_replace(index, curr_location, new_val):
            if index == 3:
                matrix[curr_location[0]][curr_location[1]] = new_val
            else:
                old_val = matrix[curr_location[0]][curr_location[1]]
                matrix[curr_location[0]][curr_location[1]] = new_val
                recurse_replace(index + 1, rotate_90(curr_location, n), old_val)

        n = len(matrix)
        loop_count = n // 2 + 1 if n % 2 else n // 2
        for i in range(loop_count):
            top_part = [(i, x) for x in range(0 + i, n - i - 1)]
            init_data = [matrix[x][i] for x in reversed(range(0 + i, n - i))]
            for index, location in enumerate(top_part):
                recurse_replace(0, location, init_data[index])


sol = Solution()
matrices = [
    #    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
    #    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #    [1],
    #    [[1, 2], [3, 4]],
    #    [['a', 'b'], ['c', 'd']],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
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
