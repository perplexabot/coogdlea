"""Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""


class Solution:
    def numDistinct(self, s: 'str', t: 'str') -> 'int':
        from collections import defaultdict
        from collections import Counter
        from functools import lru_cache

        if len(t) > len(s):
            return 0

        if t == '':
            return 1

        if s == '':
            return 0

        scnt = Counter(s)
        tcnt = Counter(t)
        for c in tcnt:
            if tcnt[c] > scnt[c]:
                return 0

        s_ind_memo = defaultdict(list)
        for ind, c in enumerate(s):
            s_ind_memo[c].append(ind)

        @lru_cache()
        def findSeq(si, ti):
            if ti == len(t):
                return 1
            if t[ti] not in s_ind_memo:
                return 0

            c = 0
            for ind in s_ind_memo[t[ti]]:
                if ind >= si:
                    c += findSeq(ind + 1, ti + 1)
            return c

        return findSeq(0, 0)


inps = [
    ('babgbag', 'bag', 5),
    ('rabbbit', 'rabbit', 3),
    ('ttt', 't', 3),
    ('', '', 1),
    ('hgel', '', 1),
    ('', 'hellow', 0),
    (
        "adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc",
        "bcddceeeebecbc",
        700_531_452,
    ),
]

sol = Solution()
for s, t, exp in inps:
    print(f"Finding seq cnt for '{t}' in '{s}' and asserting...")
    ans = sol.numDistinct(s, t)
    print(f" Got: {ans}")
    assert ans == exp
