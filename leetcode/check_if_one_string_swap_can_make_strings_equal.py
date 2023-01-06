"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose
    two indices in a string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on
    exactly one of the strings. Otherwise, return false.

Example 1:
    Input: s1 = "bank", s2 = "kanb"
    Output: true
    Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
    Input: s1 = "attack", s2 = "defend"
    Output: false
    Explanation: It is impossible to make them equal with one string swap.

Example 3:
    Input: s1 = "kelb", s2 = "kelb"
    Output: true
    Explanation: The two strings are already equal, so no string swap operation is required.

Constraints:
    1 <= s1.length, s2.length <= 100
    s1.length == s2.length
    s1 and s2 consist of only lowercase English letters.

A:
    strings not equal   ->  return false
    strings empty       ->  return true
    strings of size 1   ->  return true
    strings equal       ->  return true
    only lower case

D:
    Input: s1 = "bank", s2 = "kanb"

    cnts = 0
    b != k, cnts = 1, i0 = 0
    a == a, cnts = 1
    n == n, cnts = 1
    k != b, cnts = 2, i1 = 3
    return cnts == 2 and s0[i0] == s1[i1] and s0[i1] == s1[i0] -> true


    Input: s1 = "attack", s2 = "defend"

    cnts = 0
    a != d, cnts = 1, i0 = 0
    t != e, cnts = 2, i1 = 1
    t != f, cnts = 3, cnts > 2 -> return false

    for each index:
        if s0[ind] != s1[ind] -> increment count and save index
        if cnt > 2 -> return False
    return cnt == 2 and s0[i0] == s1[i1] and s0[i1] == s1[i0] -> true
"""


def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    cnts = 0
    conflict = []
    for ind in range(len(s1)):
        if s1[ind] == s2[ind]:
            continue

        cnts += 1
        conflict.append(ind)
        if cnts > 2:
            return False

    return cnts == 2 and s1[conflict[0]] == s2[conflict[1]] and s1[conflict[1]] == s2[conflict[0]]


cases = [
    ("bank", "kanb", True),
    ("attack", "defend", False),
    ("kelb", "kelb", True),
    ("", "", True),
    ("a", "a", True),
    ("ab", "ba", True),
    ("abc", "cbd", False),
    ("what", "hwat", True),
]

for (s1, s2, exp) in cases:
    assert (
        got := areAlmostEqual(s1, s2)
    ) == exp, f"Failed ({s1}, {s2}) - expecting ({exp}), got ({got})"
