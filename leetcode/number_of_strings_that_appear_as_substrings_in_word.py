"""
Given an array of strings patterns and a string word, return the number of strings in patterns that
    exist as a substring in word.

A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: patterns = ["a","abc","bc","d"], word = "abc"
    Output: 3
    Explanation:
    - "a" appears as a substring in "abc".
    - "abc" appears as a substring in "abc".
    - "bc" appears as a substring in "abc".
    - "d" does not appear as a substring in "abc".
    3 of the strings in patterns appear as a substring in word.

Example 2:
    Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
    Output: 2
    Explanation:
    - "a" appears as a substring in "aaaaabbbbb".
    - "b" appears as a substring in "aaaaabbbbb".
    - "c" does not appear as a substring in "aaaaabbbbb".
    2 of the strings in patterns appear as a substring in word.

Example 3:
    Input: patterns = ["a","a","a"], word = "ab"
    Output: 3
    Explanation: Each of the patterns appears as a substring in word "ab".

Constraints:
    1 <= patterns.length <= 100
    1 <= patterns[i].length <= 100
    1 <= word.length <= 100
    patterns[i] and word consist of lowercase English letters.

A:
    no patterns ->      return 0
    no word     ->      return 0
    a pattern length > word length -> don't check
    according to constraint all elements of words and patterns are comprised of lower case letters

D:
    Input: patterns = ["a","abc","bc","d"], word = "abc"
    final = 0
    "a" in word?    final += 1
    "abc" in word?  final += 1
    "bc" in word? final += 1
    "d" not in word, NOP
    return final = 3
"""


def numOfStrings(patterns: list[str], word: str) -> int:
    if not patterns or not word:
        return 0

    return sum([1 for pattern in patterns if pattern in word])


cases = [
    (["a", "abc", "bc", "d"], "abc", 3),
    (["a", "b", "c"], "aaaaabbbbb", 2),
    (["a", "a", "a"], "ab", 3),
    ([], "word", 0),
    (["a", "b"], "", 0),
    (["abc"], "acbccc", 0),
    (["a"], "b", 0),
    (["a"], "a", 1),
    (["ca"], "ac", 0),
    (["ab"], "ab", 1),
]

for (patterns, word, exp) in cases:
    assert (
        got := numOfStrings(patterns, word)
    ) == exp, f"Failed case ({patterns}, {word}) - expecting({exp}), got ({got})."
