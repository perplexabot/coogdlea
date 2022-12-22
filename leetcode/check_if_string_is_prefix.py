"""
Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in
    words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.

Example 1:
    Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
    Output: true
    Explanation:
    s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:
    Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
    Output: false
    Explanation:
    It is impossible to make s using a prefix of arr.

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    1 <= s.length <= 1000
    words[i] and s consist of only lowercase English letters.

A:
    s is ''         ->  not possible
    array is empty  -> not possible
    s or elems in array not string  ->  not possible
    total chars of words in array do no sum to length of s  ->  false
A:
    s="h", words=["ha"], return false? Yes, return false

D:
    Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]

    clen = 0, curr = []
    clen < len(s) -> curr += words[0], clen += len(words[0]) = 1
    clen < len(s) -> curr += words[1], clen += len(words[1]) = 5
    clen < len(s) -> curr += words[2], clen += len(words[2]) = 13
    clen == len(s) -> ''.join(curr) == s -> return True

    Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
    clen = 0, curr = []
    clen < len(s) -> curr += words[0], clen += len(words[0]) = 6
    clen < len(s) -> curr += words[1], clen += len(words[1]) = 7
    clen < len(s) -> curr += words[2], clen += len(words[2]) = 15
    clen > len(s) -> return False
"""


def isPrefixString(s: str, words: list[str]) -> bool:
    clen = 0
    curr = []
    for word in words + ['']:
        if clen < len(s):
            curr += word
            clen += len(word)
        elif clen == len(s):
            return s == ''.join(curr)
        else:
            return False


cases = [
    ("hi", ["h", "i"], True),
    ("h", ["h"], True),
    ("h", ["h", "b"], True),
    ("h", ["haaa", "b"], False),
    ("iloveleetcode", ["i", "love", "leetcode", "apples"], True),
    ("iloveleetcode", ["apples", "i", "love", "leetcode"], False),
]

for (s, words, exp) in cases:
    assert (
        got := isPrefixString(s, words)
    ) == exp, f"Failed case ({s}, {words}) - expecting ({exp}), got ({got})"
