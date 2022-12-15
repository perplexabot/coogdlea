"""The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.


Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        from itertools import groupby

        i = 0
        curr = '1'
        while i < n - 1:
            i += 1
            cnts = []
            if len(curr) == 1:
                cnts.append((1, '1'))
            else:
                for key, rep in groupby(curr):
                    cnts.append((str(len(list(rep))), key))
            curr = ''.join([''.join([str(cnt), val]) for cnt, val in cnts])
        return curr


sol = Solution()

for n in range(1, 10):
    ans = sol.countAndSay(n)
    print(f"For n = {n}, {ans}")
