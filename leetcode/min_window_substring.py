"""Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique
minimum window in S.
Characters that are duplicated in T should also be duplicated in S.
"""


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter

        l, r = 0, 0
        tcnt = Counter(t)
        scnt = Counter(s[l : r + 1])
        minWin = (0, float('inf'))
        while r < len(s):
            if sum((tcnt - scnt).values()):
                r += 1
                if r < len(s):
                    scnt[s[r]] += 1
            else:
                minWin = min(minWin, (l, r), key=lambda x: x[1] - x[0])
                scnt[s[l]] -= 1
                l += 1

        return '' if float('inf') in minWin else s[minWin[0] : minWin[1] + 1]


inps = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("this is a test string", "tist", "t stri"),
    ('bbbbbbbbabbbbbbbb', 'a', 'a'),
    ('abcdefghijkl', 'bdfh', 'bcdefgh'),
    ('', 'abc', ''),
    ('xyz', 'abc', ''),
    ('xyz', 'xyz', 'xyz'),
    ('a', 'a', 'a'),
    ('abcghijklabc', 'abc', 'abc'),
    ('abcghbjklabc', 'abc', 'abc'),
    ('aghbjklc', 'abc', 'aghbjklc'),
]

sol = Solution()
for s, t, exp in inps:
    print(f"Finding min window in {s} for elems in {t} and asserting...")
    ans = sol.minWindow(s, t)
    print(f"got: {ans}")
    assert ans == exp
