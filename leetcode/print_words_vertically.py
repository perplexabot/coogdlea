"""
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Example 1:
    Input: s = "HOW ARE YOU"
    Output: ["HAY","ORO","WEU"]
    Explanation: Each word is printed vertically.
    "HAY"
    "ORO"
    "WEU"
Example 2:
    Input: s = "TO BE OR NOT TO BE"
    Output: ["TBONTB","OEROOE","   T"]
    Explanation: Trailing spaces is not allowed.
    "TBONTB"
    "OEROOE"
    "   T"
Example 3:
    Input: s = "CONTEST IS COMING"
    Output: ["CIC","OSO","N M","T I","E N","S G","T"]

Constraints:
    1 <= s.length <= 200
    s contains only upper case English letters.
    It's guaranteed that there is only one space between 2 words.

URL: https://leetcode.com/problems/print-words-vertically/
"""


class Solution:
    def printVertically(self, s: str) -> list[str]:
        from itertools import zip_longest

        return [''.join(x).rstrip() for x in zip_longest(*s.split(' '), fillvalue=' ')]


inps = [
    ("HOW ARE YOU", ["HAY", "ORO", "WEU"]),
    ("TO BE OR NOT TO BE", ["TBONTB", "OEROOE", "   T"]),
    ("CONTEST IS COMING", ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]),
]

sol = Solution()
for inp, exp in inps:
    assert (ans := sol.printVertically(inp)) == exp, f"failed '{inp}' --- exp {exp} --- got {ans}'"
