"""
Given a string s, check if it can be constructed by taking a substring of it and appending
multiple copies of the substring together.

Example 1:
    Input: s = "abab"
    Output: true
    Explanation: It is the substring "ab" twice.
Example 2:
    Input: s = "aba"
    Output: false
Example 3:
    Input: s = "abcabcabcabc"
    Output: true
    Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
Constraints:
    1 <= s.length <= 104
    s consists of lowercase English letters.

abcabcabcabc

for psize in range(1, len(s)//2):
    pattern = s[:psize]
    if not len(s) % psize:
        for i in range(psize, len(s), psize):
            i



for each pattern:
    if not len(s) % len(pattern):
        if pattern makes up s:
            return true

return false

"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for psize in range((len(s) // 2), 0, -1):
            pattern = s[:psize]
            if not len(s) % psize:
                good = True
                for start in range(psize, len(s), psize):
                    if s[start : start + psize] != pattern:
                        good = False
                        break
                if good:
                    return True

        return False


inps = [
    ('ab', False),
    ('aa', True),
    ('abab', True),
    ("aba", False),
    ("abcabcabcabc", True),
    ("a", False),
    ("", False),
    ("abcdabcd", True),
    ("aaaa", True),
    ("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", True),
    ("asdkjbceoinlkjspoinlkjflakjenmoineibapbasbkjdl", False),
]

sol = Solution()
for s, exp in inps:
    assert (
        ans := sol.repeatedSubstringPattern(s)
    ) == exp, f"failed with {s}, expecting {exp}, got {ans}"
