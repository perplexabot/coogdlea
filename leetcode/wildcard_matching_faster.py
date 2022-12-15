"""Given an input string (s) and a pattern (p), implement wildcard pattern matching with
support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*'
matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        from collections import deque

        p = p.replace('?', '.').split('*')
        p = deque(p)

        if len(p) == 1:
            return True if re.fullmatch(p[0], s) else False

        # make sure left end follows pattern
        res = re.match(p.popleft(), s)
        if not res:
            return False
        s = s[res.end() :]

        # make sure right end follows pattern
        res = re.search(p.pop() + '$', s)
        if not res:
            return False
        s = s[: res.start()]

        # make sure everything else is contained in string (no overlaps)
        while p:
            res = re.search(p.popleft(), s)
            if not res:
                return False
            s = s[res.end() :]
        return True


# string, patter, expected
inps = [
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False),
    ("abcdef", "", False),
    ("abcdef", "*", True),
    ("abcdef", "??????", True),
    ("abcdef", "a?c?e?", True),
    ("abcdef", "a?c?e?", True),
    ("abcdef", "********************", True),
    ("abcdef", "*****abcdef*****", True),
    ("abcdef", "?abcdef?", False),
    ("", "", True),
    ("", "*", True),
    ("", "*****", True),
    ("", "?", False),
    ("a", "*********?********", True),
    ("a", "?", True),
    ("abc", "?*?", True),
    (
        "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba",
        "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*",
        True,
    ),
    (
        "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
        "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb",
        False,
    ),
]

sol = Solution()
for s, p, exp in inps:
    print(f"Doing string[{s}] with pattern[{p}] and asserting...")
    assert sol.isMatch(s, p) == exp
