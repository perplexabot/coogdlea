"""
You are given two 0-indexed strings s and target. You can take some letters from s and rearrange
    them to form new strings.

Return the maximum number of copies of target that can be formed by taking letters from s and
    rearranging them.

Example 1:
    Input: s = "ilovecodingonleetcode", target = "code"
    Output: 2
    Explanation:
    For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
    For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
    The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
    We can make at most two copies of "code", so we return 2.

Example 2:
    Input: s = "abcba", target = "abc"
    Output: 1
    Explanation:
    We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
    We can make at most one copy of "abc", so we return 1.
    Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot reuse the
        letter 'c' at index 2, so we cannot make a second copy of "abc".

Example 3:
    Input: s = "abbaccaddaeea", target = "aaaaa"
    Output: 1
    Explanation:
    We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.
    We can make at most one copy of "aaaaa", so we return 1.

Constraints:
    1 <= s.length <= 100
    1 <= target.length <= 10
    s and target consist of lowercase English letters.

A:
    if s is empty -> return 0 (not possible)
    if target is empty -> return ? (not possible)
    if len(target) > len(s) -> return 0

D:
    count chars in s
    times = 0
    while any (count chars) are > 0:
        count[chars] -= 1
        times += 1
    return times
"""


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter

        c = Counter(s)
        times = 0
        while all(v > 0 for v in c.values()):
            for char in target:
                if c[char] > 0:
                    c[char] -= 1
                else:
                    return times
            times += 1
        return times


cases = [
    ("ilovecodingonleetcode", "code", 2),
    ("abcba", "abc", 1),
    ("abbaccaddaeea", "aaaaa", 1),
    ("abc", "d", 0),
    ("a", "aaa", 0),
    ("a", "a", 1),
]

sol = Solution()
for (s, target, exp) in cases:
    assert (
        got := sol.rearrangeCharacters(s, target)
    ) == exp, f"Failed case ({s}, {target}) - expecting ({exp}), got ({got})."
