"""
Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of
    occurrences (i.e., the same frequency).

Example 1:
    Input: s = "abacbc"
    Output: true
    Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur
        2 times in s.

Example 2:
    Input: s = "aaabb"
    Output: false
    Explanation: The characters that appear in s are 'a' and 'b'.
    'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters.

A:
    empty string -> True
    string of len 1 -> True
    other than lower case chars in string -> not possible according to constraint
D:
    get counts
    ensure list of counts is same value
"""


def areOccurrencesEqual(s: str) -> bool:
    if not s:
        return True

    from collections import Counter

    cnts = Counter(s)
    return len(set(cnts.values())) == 1


cases = [
    ("abacbc", True),
    ("aaabb", False),
    ("", True),
    ("a", True),
    ("aa", True),
    ("ab", True),
    ("abb", False),
]

for (s, exp) in cases:
    assert (ans := areOccurrencesEqual(s)) == exp, f"Failed with {s} - got {ans}, expecting {exp}"
