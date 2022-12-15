"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
    palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.

A:
    s.len is empty  ->  return 0
    s.len is 1      ->  return 1

D:
    s = "abccccdd"
    l = len(s) = 8
    c = counts(s) = {'c': 4, 'd': 2, 'a': 1, 'b': 1}
                      > 1     > 1     <= 1    <= 1
    x = 0             + 4//2  2//2                  =   0 + 2 + 1 = 3
    max_palindrome_size = 2*x + 1 if len(s) > x else 2*x
"""


def longestPalindrome(s: str) -> int:
    if not s:
        return 0

    from collections import Counter

    c = Counter(s)
    x = sum([c[key] // 2 for key in c if c[key] > 1])
    return 2 * x + 1 if len(s) > 2 * x else 2 * x


cases = [("abccccdd", 7), ("a", 1), ("", 0), ("Aa", 1), ("AAa", 3), ("aaa", 3), ("aa", 2)]

for (s, exp) in cases:
    assert (ans := longestPalindrome(s)) == exp, f"Failed ({s}) - expecting ({exp}), got ({ans})"
