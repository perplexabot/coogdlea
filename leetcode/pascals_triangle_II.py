"""Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        ans = [1]

        if rowIndex == 1:
            return ans

        for row_ind in range(2, rowIndex + 1):
            row = [1]
            for j in range(1, row_ind - 1):
                row.append(ans[j - 1] + ans[j])
            row.append(1)
            ans = row
        return ans


sol = Solution()
for i in range(7):
    print(f"Trying row {i}")
    print(f" got: {sol.getRow(i)}")
