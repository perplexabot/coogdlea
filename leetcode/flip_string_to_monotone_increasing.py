"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0),
followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

Example 1:
    Input: "00110"
    Output: 1
    Explanation: We flip the last digit to get 00111.
Example 2:
    Input: "010110"
    Output: 2
    Explanation: We flip to get 011111, or alternatively 000111.
Example 3:
    Input: "00011000"
    Output: 2
    Explanation: We flip to get 00000000.

Note:
    1 <= S.length <= 20000
    S only consists of '0' and '1' characters.

URL: https://leetcode.com/problems/flip-string-to-monotone-increasing/
START: 19:20
"""


class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        if len(S) == 1 or S.count('0') == len(S) or S.count('1') == len(S):
            return 0

        s = S.lstrip('0')
        cnt0 = s.count('0')

        s = '1' + s[1:] if s[0] == 0 else '0' + s[1:]
        cnt1 = self.minFlipsMonoIncr(s) + 1

        return min(cnt0, cnt1)


sol = Solution()

inps = [
    ('00110', 1),
    ('010110', 2),
    ('00011000', 2),
    ('0', 0),
    ('1', 0),
    ('01', 0),
    ('10', 1),
    ('', 0),
]

for inp, exp in inps:
    assert (got := sol.minFlipsMonoIncr(inp)) == exp, f"    got {got}, expected {exp}"
