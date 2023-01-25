"""
The letter value of a letter is its position in the alphabet starting
    from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the concatenation of the letter
    values of each letter in s, which is then converted into an integer.

    For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After
        converting it, we get 21.

You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase
    English letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord equals the
    numerical value of targetWord, or false otherwise.

Example 1:
    Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
    Output: true
    Explanation:
    The numerical value of firstWord is "acb" -> "021" -> 21.
    The numerical value of secondWord is "cba" -> "210" -> 210.
    The numerical value of targetWord is "cdb" -> "231" -> 231.
    We return true because 21 + 210 == 231.

Example 2:
    Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
    Output: false
    Explanation:
    The numerical value of firstWord is "aaa" -> "000" -> 0.
    The numerical value of secondWord is "a" -> "0" -> 0.
    The numerical value of targetWord is "aab" -> "001" -> 1.
    We return false because 0 + 0 != 1.

Example 3:
    Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
    Output: true
    Explanation:
    The numerical value of firstWord is "aaa" -> "000" -> 0.
    The numerical value of secondWord is "a" -> "0" -> 0.
    The numerical value of targetWord is "aaaa" -> "0000" -> 0.
    We return true because 0 + 0 == 0.

Constraints:
    1 <= firstWord.length, secondWord.length, targetWord.length <= 8
    firstWord, secondWord, and targetWord consist of lowercase English letters from 'a'
    to 'j' inclusive.

A:
    target is empty         ->  true if first and  second are also empty else false
    first or second empty   ->  target must equal the non empty one
    !above two cases not possible according to constraint!

D:
    Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
    first = int('000')
    second = int('0')
    target = int('001')
    target != first + second
    return false

P:
    create dict
    generate ints for each
    confirm sum
"""


class Solution:
    def __init__(self):
        self.chars = "abcdefghij"
        self.char_to_val = {char: str(index) for index, char in enumerate(self.chars)}

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        fval = int(''.join([self.char_to_val[c] for c in firstWord]))
        sval = int(''.join([self.char_to_val[c] for c in secondWord]))
        tval = int(''.join([self.char_to_val[c] for c in targetWord]))
        return tval == sval + fval


cases = [
    ("acb", "cba", "cdb", True),
    ("aaa", "a", "aab", False),
    ("aaa", "a", "aaaa", True),
    ("a", "a", "a", True),
    ("a", "b", "b", True),
    ("aba", "a", "ba", True),
]

sol = Solution()
for (firstWord, secondWord, targetWord, expected) in cases:
    assert (
        got := sol.isSumEqual(firstWord, secondWord, targetWord)
    ) == expected, f"Trying case ({firstWord}, {secondWord}, {targetWord}) - got ({got}), expecting ({expected})"
