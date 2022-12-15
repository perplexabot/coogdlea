"""Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        ans = [[1]]

        if numRows == 1:
            return ans

        for row_ind in range(2, numRows + 1):
            row = [1]
            for j in range(1, row_ind - 1):
                row.append(ans[-1][j - 1] + ans[-1][j])
            row.append(1)
            ans.append(row)
        return ans


sol = Solution()
for i in range(7):
    print(f"For n = {i}")
    ans = sol.generate(i)
    print(ans)
    print('------------------')
