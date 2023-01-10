"""
You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.

Example 1:
    Input: words = ["pay","attention","practice","attend"], pref = "at"
    Output: 2
    Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

Example 2:
    Input: words = ["leetcode","win","loops","success"], pref = "code"
    Output: 0
    Explanation: There are no strings that contain "code" as a prefix.

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length, pref.length <= 100
    words[i] and pref consist of lowercase English letters.

A:
    prefix is empty ->  not possible according to constraint
    words is empty  ->  not possible according to constraint
    words contains empty strings -> not possible according to constraint
"""


def prefixCount(words: list[str], pref: str) -> int:
    return sum(1 for word in words if word.startswith(pref))


cases = [
    (["leetcode", "win", "loops", "success"], "code", 0),
    (["pay", "attention", "practice", "attend"], "at", 2),
    (["h"], "h", 1),
    (["ah"], "a", 1),
    (["ah"], "h", 0),
]

for (words, prefix, exp) in cases:
    assert (
        got := prefixCount(words, prefix)
    ) == exp, f"Failed case ({words}, {prefix}) - expecting ({exp}), got ({got})."
