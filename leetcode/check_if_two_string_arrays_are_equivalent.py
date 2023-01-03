"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string,
    and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:
    Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
    Output: true
    Explanation:
    word1 represents string "ab" + "c" -> "abc"
    word2 represents string "a" + "bc" -> "abc"
    The strings are the same, so return true.

Example 2:
    Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
    Output: false

Example 3:
    Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
    Output: true

Constraints:
    1 <= word1.length, word2.length <= 10^3
    1 <= word1[i].length, word2[i].length <= 10^3
    1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
    word1[i] and word2[i] consist of lowercase letters.

A:
    both word1 and word2 empty      ->  return true
    either word1 or word2 empty     ->  return false
    wordn contains none alpha       ->  not possible according to constraint
"""


def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    return ''.join(word1) == ''.join(word2)


cases = [
    (["ab", "c"], ["a", "bc"], True),
    (["a", "cb"], ["ab", "c"], False),
    (["abc", "d", "defg"], ["abcddefg"], True),
    (["a"], ["b"], False),
    (["a", "b"], ["ab"], True),
    ([], ["a"], False),
    (["a"], [], False),
    ([], [], True),
    (["a"], ["a"], True),
    (["ab"], ["ba"], False),
]

for (word1, word2, exp) in cases:
    assert (
        got := arrayStringsAreEqual(word1, word2)
    ) == exp, f"Failed case ({word1}, {word2}) - expecting ({exp}), got ({got})."
