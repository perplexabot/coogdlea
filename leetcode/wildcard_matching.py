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

        p = '^' + p.replace('?', '.').replace('*', '.*') + '$'
        MY_RE = re.compile(p)
        return True if MY_RE.match(s) else False


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
]

sol = Solution()
for s, p, exp in inps:
    print(f"Doing string[{s}] with pattern[{p}] and asserting...")
    assert sol.isMatch(s, p) == exp
