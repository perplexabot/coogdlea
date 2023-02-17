"""
A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique.

Example 1:
                01234
    Input: s = "leeetcode"
    Output: "leetcode"
    Explanation:
    Remove an 'e' from the first group of 'e's to create "leetcode".
    No three consecutive characters are equal, so return "leetcode".

Example 2:
    Input: s = "aaabaaaa"
    Output: "aabaa"
    Explanation:
    Remove an 'a' from the first group of 'a's to create "aabaaaa".
    Remove two 'a's from the second group of 'a's to create "aabaa".
    No three consecutive characters are equal, so return "aabaa".

Example 3:
    Input: s = "aab"
    Output: "aab"
    Explanation: No three consecutive characters are equal, so return "aab".

Constraints:
    1 <= s.length <= 10**5
    s consists only of lowercase English letters.

A:
    s is empty      ->  return string
    s is length 1   ->  return string
    s is lenthh 2   ->  return string
    s is single char    ->  return single char twice

D:
    if len(s) < 3:
        return s

    curr = s[0]
    curr_s = 0
    curr_e = 0
    reps = []
    for ind, e in enumerate(s[1:]):
        if e == curr:
            curr_e = ind + 1
        else:
            reps.append((curr_s,curr_e))
            curr_s = ind + 1
            curr_e = ind + 1

    new_str = []
    for st,en in reps:
        if en - st > 1:
            new_str.append(s[st] * 2)
        else:
            new_str.append(s[st:en+1])
    return ''.join(new_str)
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        reps = []
        prev = s[0]
        curr_s = 0
        curr_e = 0
        for ind, e in enumerate(s[1:]):
            if e == prev:
                curr_e = ind + 1
            else:
                reps.append((curr_s, curr_e))
                curr_s = ind + 1
                curr_e = ind + 1
                prev = e
        reps.append((curr_s, curr_e))

        new_str = []
        for st, en in reps:
            if en - st > 1:
                new_str.append(s[st] * 2)
            else:
                new_str.append(s[st : en + 1])
        return ''.join(new_str)


cases = [
    ("leeetcode", "leetcode"),
    ("aaabaaaa", "aabaa"),
    ("aab", "aab"),
    ("a", "a"),
    ("ab", "ab"),
    ("aaa", "aa"),
    ("aa", "aa"),
    ("abc", "abc"),
    ("aba", "aba"),
    ("aaaaaaaaaaaaaaaaaaaaa", "aa"),
]

sol = Solution()
for (s, exp) in cases:
    assert (
        got := sol.makeFancyString(s)
    ) == exp, f"Failed case ({s}) -  got ({got}), expecting ({exp})"
