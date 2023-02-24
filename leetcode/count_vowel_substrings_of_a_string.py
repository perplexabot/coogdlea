"""
A substring is a contiguous (non-empty) sequence of characters within a string.
A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and
    has all five vowels present in it.
Given a string word, return the number of vowel substrings in word.

Example 1:
    Input: word = "aeiouu"
    Output: 2
    Explanation: The vowel substrings of word are as follows (underlined):
    - "aeiouu"
    - "aeiouu"

Example 2:
    Input: word = "unicornarihan"
    Output: 0
    Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:
    Input: word = "cuaieuouac"
    Output: 7
    Explanation: The vowel substrings of word are as follows (underlined):
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"

Constraints:
    1 <= word.length <= 100
    word consists of lowercase English letters only.

A:
    empty string -> return 0
    string length less then len(vowel_list) -> return 0
    string doesn't contain all vowels -> return 0

D:
    if len(s) < 5:
        return 0

    ways = 0
    for start in range(len(s)):
        if s[start] is vowel:
            end = start + 1
            while end < len(s) and s[end] is vowel:
                if not symmetric_difference(s[start:end], vowels):
                    ways ++
                end ++
            vowel_only_segments.push((start,end))
"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word) < 5:
            return 0

        vowels = set(list('aeiou'))
        ways = 0
        for start in range(len(word)):
            if word[start] in vowels:
                end = start + 1
                while end < len(word) and word[end] in vowels:
                    if not vowels.symmetric_difference(word[start : end + 1]):
                        ways += 1
                    end += 1
        return ways


cases = [("aeiou", 1), ("abeiou", 0), ("unicornarihan", 0), ("cuaieuouac", 7)]

sol = Solution()
for (word, exp) in cases:
    assert (
        got := sol.countVowelSubstrings(word)
    ) == exp, f"Failed case ({word}) - expecting ({exp}), got ({got})"
