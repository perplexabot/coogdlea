"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.

Example 2:
    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.

Example 3:
    Input: s = "luffy is still joyboy"
    Output: 6
    Explanation: The last word is "joyboy" with length 6.

Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

A:
    empty string -> ""
    string of whitespace -> ""
"""


def lengthOfLastWord(s: str) -> int:
    return 0 if not s or not s.strip() else len(s.split()[-1])


cases = [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("", 0),
    ("a", 1),
    (None, 0),
    ("    ", 0),
]

for (s, exp) in cases:
    assert (ans := lengthOfLastWord(s)) == exp, f"Failed ({s}) - expecting ({exp}), got ({exp})"
