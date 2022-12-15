"""Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the
kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n**2.
"""


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        cnt = 0
        linear = [None]
        while cnt < len(matrix) ** 2 - k + 1:
            currMax = float('-inf')
            maxInd = None
            for ind, row in enumerate(matrix):
                if row and row[-1] > currMax:
                    maxInd = ind
                    currMax = matrix[maxInd][-1]

            # uncomment to remove dups from linear list
            # if matrix[maxInd][-1] != linear[-1]:
            linear.append(matrix[maxInd].pop())
            cnt += 1

        # return kth from right
        return linear[-1]


inps = [
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
    ([[1, 1], [1, 2]], 2, 1),
    ([[1, 2], [1, 3]], 2, 1),
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 4),
]

sol = Solution()
for mat, k, exp in inps:
    print(f"Finding {k}th min in {mat} and asserting...")
    ans = sol.kthSmallest(mat, k)
    print(f" got: {ans}")
    assert exp == ans
