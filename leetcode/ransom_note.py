"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using
    the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

A:
    can a letter in a magazine be used more than once if it appears only once in magazine   -> no
    ransomNote = "" -> return True
    magazine = "" -> return True if not ransomNote else false
    lower case english only according to constraint

D:
    Input: ransomNote = "a", magazine = "b"
    cntsR = {'a': 1}
    cntsM = {'b': 1}

    cntsR['a'] -> 1 <= cntsM['a'] -> return false
"""


def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import Counter

    if not ransomNote:
        return True

    if not magazine:
        return False

    cntsR = Counter(ransomNote)
    cntsM = Counter(magazine)
    return all(cntsR[charR] <= cntsM[charR] for charR in cntsR)


cases = [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("", "abc", True),
    ("abc", "", False),
    ("", "", True),
    ("abc", "cba", True),
    ("a", "aa", True),
    ("aa", "a", False),
    ("aabb", "bbaacc", True),
    ("abcc", "cbaa", False),
]

for (note, magazine, exp) in cases:
    assert (
        got := canConstruct(note, magazine)
    ) == exp, f"Failed case ({note}, {magazine}) - expecting ({exp}), got ({got})."
