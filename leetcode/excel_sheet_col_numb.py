"""Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        from string import ascii_uppercase

        s_len = len(s) - 1
        conv = {c: ind + 1 for ind, c in enumerate(ascii_uppercase)}
        return sum(26 ** (s_len - ind) * conv[c] for ind, c in enumerate(s))


inps = [
    ('A', 1),
    ('B', 2),
    ('Z', 26),
    ('AA', 27),
    ('AB', 28),
    ('ZY', 701),
    ('ZZ', 702),
    ('AMJ', 1024),
]

sol = Solution()
for s, exp in inps:
    print(f"Getting number for {s} and asserting")
    assert sol.titleToNumber(s) == exp
