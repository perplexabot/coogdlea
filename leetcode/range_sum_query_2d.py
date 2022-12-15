"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper
left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and
(row2, col2) = (4, 3), which contains sum = 8.

Example:

    Given matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]

    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12

Note:
    You may assume that the matrix does not change.
    There are many calls to sumRegion function.
    You may assume that row1  row2 and col1  col2.


    A
        possible to use cache?
        matrices of size 0x0, 1x1, 1xn, nx1 (also [] vs [[]])
        ul and lr are the same
        ul and lr are the matrix
        assuming ul and lr passed are valid (within matrix and order is good)
    D
        using matrix above with sumRegion(2,1,4,3)
            2 + 0 + 1 = 3
            1 + 0 + 1 = 2
            0 + 3 + 0 = 3
                        8

    P
        row = ul_x
        while row <= lr_x:
            row_sum = 0
            col = ul_y
            cache[row] = cache[row] if row in cache else {}
            while col <= lr_y:
                if col in cache[row] and if good value found in cache[row][col]:
                    row_sum += cache[row][col][good]
                    col = good
                else
                    row_sum += matrix[row][col]
                col += 1

            if cache[row][col] is not None:
                cache[row][ul_y][lr_y] = row_sum
            else:
                cache[row][ul_y] = {lr_y:row_sum}

            row += 1
"""


class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.cache = {}

    def get_good(self, row: int, col: int, max_col: int) -> int:
        good_val = float('-inf')
        for y in self.cache[row][col]:
            if y > max_col:
                continue

            good_val = max(good_val, y)
        return good_val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row = row1
        total = 0
        while row <= row2:
            row_sum = 0
            self.cache[row] = self.cache[row] if row in self.cache else {}
            col = col1
            while col <= col2:
                if col in self.cache[row] and (good := self.get_good(row, col, col2)) >= 0:

                    row_sum += self.cache[row][col][good]
                    col = good
                else:
                    row_sum += self.matrix[row][col]
                col += 1

            if col1 in self.cache[row]:
                self.cache[row][col1][col2] = row_sum
            else:
                self.cache[row][col1] = {col2: row_sum}
            total += row_sum
            row += 1
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

x = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]

obj = NumMatrix(x)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
