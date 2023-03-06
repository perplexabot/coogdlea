"""
International Morse Code defines a standard encoding where each letter is mapped to a series of
    dots and dashes, as follows:
    - 'a' maps to ".-",
    - 'b' maps to "-...",
    - 'c' maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:
    [".-","-...","-.-.","-..",".","..-.","--.","....",
        "..",".---","-.-",".-..","--","-.","---",".--.",
        "--.-",".-.","...","-","..-","...-",".--","-..-",
        "-.--","--.."]

Given an array of strings words where each word can be written as a concatenation of the Morse
    code of each letter.
    - For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-",
        and "-...". We will call such a concatenation the transformation of a word.

Return the number of different transformations among all words we have.

Example 1:
    Input: words = ["gin","zen","gig","msg"]
    Output: 2
    Explanation: The transformation of each word is:
    "gin" -> "--...-."
    "zen" -> "--...-."
    "gig" -> "--...--."
    "msg" -> "--...--."
    There are 2 different transformations: "--...-." and "--...--.".

Example 2:
    Input: words = ["a"]
    Output: 1

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 12
    words[i] consists of lowercase English letters.

A:
    empty words     -> return 0
    len(words) = 1  -> return 1

D:
    create mapping
    for each word, transform and add to set
    return size of set
"""

from typing import List


class Solution:
    def __init__(self):
        from string import ascii_lowercase

        morse_vals = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        self.map = {char: code for char, code in zip(ascii_lowercase, morse_vals)}

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformations = set()
        for word in words:
            transformation = []
            for char in word:
                transformation.append(self.map[char])
            transformations.add(''.join(transformation))
        return len(transformations)


cases = [(["gin", "zen", "gig", "msg"], 2), (["a"], 1)]

sol = Solution()
for (case, exp) in cases:
    assert (
        got := sol.uniqueMorseRepresentations(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
