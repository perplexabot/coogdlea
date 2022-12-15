"""
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to
    goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping
    the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:
    Input: s = "ab", goal = "ba"
    Output: true
    Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:
    Input: s = "ab", goal = "ab"
    Output: false
    Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results
        in "ba" != goal.

Example 3:
    Input: s = "aa", goal = "aa"
    Output: true
    Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Constraints:
    1 <= s.length, goal.length <= 2 * 10^4
    s and goal consist of lowercase letters.

A:
    one empty string        ->  false
    two empty strings       ->  false
    two equal strings       ->  false
    s1.length != s2.length  ->  false

D:
    s = 'ab', b = 'ba'

    diffs = []
    for i in range(len(s)):
        if s[i] != goal[i]
        diffs.append((s[i], goal[i]))

    if len(diffs) != 2:
        return false
    else:
        if diffs[0][0] == diffs[1][1] and diffs[1][0] == diffs[0][0]:
            return True
        else:
            return False
"""


def buddyStrings(s: str, goal: str) -> bool:
    from collections import Counter

    if len(s) != len(goal):
        return False

    cnts = Counter(s)
    diffs = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diffs.append((s[i], goal[i]))

    if len(diffs) == 1:
        return False
    elif not len(diffs):
        if any(x > 1 for x in cnts.values()):
            return True
        else:
            return False
    elif len(diffs) > 2:
        return False
    elif diffs[0][0] == diffs[1][1] and diffs[1][0] == diffs[0][1]:
        return True
    else:
        return False


cases = [
    ("ab", "ba", True),
    ("ab", "ab", False),
    ("aa", "aa", True),
    ("a", "a", False),
    ("aaa", "aaa", True),
    ("", "", False),
    ("cab", "bac", True),
    ("abac", "abad", False),
    ("abcd", "badc", False),
    ("ab", "babbb", False),
]

for (s, goal, exp) in cases:
    assert (
        got := buddyStrings(s, goal)
    ) == exp, f"Failed with ({s}, {goal}) - expecting ({exp}), got ({got})"
