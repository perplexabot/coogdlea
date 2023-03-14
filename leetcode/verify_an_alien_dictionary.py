"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a
    different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true
    if and only if the given words are sorted lexicographically in this alien language.

Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the
        sequence is unsorted.

Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.)
        According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined
        as the blank character which is less than any other character (More info).

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.

A:
    empty words -> return true
    word len of 1 -> return true
    order always valid (true)
    all letters are lower case (true)

D:
    create dict of weight 

    if len(words) < 2:
        return true

    i = 1
    first = words[0]
    second = words[1]
    while i < len(words):
        if second < first:
            return false
    return true
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        weights = {char: i for (i, char) in enumerate(order)}
        print(weights)

        if len(words) < 2:
            return True

        i = 1
        first = words[0]
        second = words[1]
        while True:

            for j in range(len(first)):
                if j >= len(second):
                    return False
                if weights[first[j]] > weights[second[j]]:
                    return False
                elif weights[first[j]] < weights[second[j]]:
                    break

            i += 1

            if i >= len(words):
                return True

            first = second
            second = words[i]
        return True


cases = [
    (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
    (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
    (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
    (["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz", True),
]

sol = Solution()
for (words, order, exp) in cases:
    assert (
        got := sol.isAlienSorted(words, order)
    ) == exp, f"Failed case ({words}, {order}), expecting ({exp}), got ({got})."
