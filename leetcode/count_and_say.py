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

        def get_bound_inds(s):
            if len(s) < 2:
                return None
            b_inds = []
            prev = s[0]
            for ind, c in enumerate(s[1:]):
                if c != prev:
                    prev = c
                    b_inds.append(ind + 1)
            return b_inds

        l = ['1']
        while len(l) < n:
            b_inds = get_bound_inds(l[-1])
            if not b_inds:
                l.append(''.join([str(len(l[-1])), l[-1][0]]))
                continue
            outstr = ''.join([str(b_inds[0]), l[-1][b_inds[0] - 1]])
            if len(b_inds) >= 2:
                for pind, b_ind in enumerate(b_inds[1:]):
                    outstr = ''.join([outstr, str(b_ind - b_inds[pind]), l[-1][b_ind - 1]])
            outstr = ''.join([outstr, str(len(l[-1]) - b_inds[-1]), l[-1][b_inds[-1]]])
            l.append(outstr)
        return l[-1]


sol = Solution()

ans = sol.countAndSay(1)
print("1: a", ans)
print("--------------------------")

ans = sol.countAndSay(2)
print("2: a", ans)
print("--------------------------")

ans = sol.countAndSay(3)
print("3: a", ans)
print("--------------------------")

ans = sol.countAndSay(4)
print("4: a", ans)
print("--------------------------")

ans = sol.countAndSay(5)
print("5: a", ans)
