"""
You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase
    English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no
    digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:
    Input: s = "a0b1c2"
    Output: "0a1b2c"
    Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c",
        "0c2a1b" are also valid permutations.

Example 2:
    Input: s = "leetcode"
    Output: ""
    Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:
    Input: s = "1229857369"
    Output: ""
    Explanation: "1229857369" has only digits so we cannot separate them by characters.
 
Constraints:
    1 <= s.length <= 500
    s consists of only lowercase English letters and/or digits.

A:
    s is empty  :   return ""
    abs(s.letters - s.numbers) > 1: return ""
    depending on if s.letters or s.numbers is larger,

D:
    Input: s = "a0b1c2"
    letters = "abc"
    numbers = "012"
    lengths are good
    return a0b2c2
"""


def reformat(s: str) -> str:
    numbers = []
    letters = []
    for c in s:
        if c.isalpha():
            letters.append(c)
        else:
            numbers.append(c)

    if abs(len(numbers) - len(letters)) > 1:
        return ""

    final = []
    if len(numbers) > len(letters):
        final.append(numbers.pop())
        while letters:
            final.append(letters.pop())
            if numbers:
                final.append(numbers.pop())
    else:
        final.append(letters.pop())
        while numbers:
            final.append(numbers.pop())
            if letters:
                final.append(letters.pop())

    return ''.join(final)


cases = ["a0b1c2", "leetcode", "1229857369"]

for case in cases:
    numbers = []
    letters = []
    for c in case:
        if c.isalpha():
            letters.append(c)
        else:
            numbers.append(c)

    if abs(len(numbers) - len(letters)) > 1:
        assert reformat(case) == ""
    else:
        ans = reformat(case)
        if case[0].isalpha():
            for i in range(0, len(case), 2):
                assert case[i].isalpha()
            for i in range(1, len(case), 2):
                assert case[i].isdigit()
        else:
            for i in range(0, len(case), 2):
                assert case[i].isdigit()
            for i in range(1, len(case), 2):
                assert case[i].isalpha()
