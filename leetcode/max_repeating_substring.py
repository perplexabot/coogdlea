"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of
sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in
sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

Example 1:
    Input: sequence = "ababc", word = "ab"
    Output: 2
    Explanation: "abab" is a substring in "ababc".

Example 2:
    Input: sequence = "ababc", word = "ba"
    Output: 1
    Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".

Example 3:
    Input: sequence = "ababc", word = "ac"
    Output: 0
    Explanation: "ac" is not a substring in "ababc".

Constraints:
    1 <= sequence.length <= 100
    1 <= word.length <= 100
    sequence and word contains only lowercase English letters.

A:
    empty seq       ->      return 0
    empty word      ->      return 0

D:
    Input: sequence = "ababc", word = "ba"
    cnt = 0
    index = 0
        ab != ba
    index = 1
        ba == ba
        index + 1, cnt ++
        ab != ba
        return 1
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_count = 0
        for i in range(len(sequence) - len(word) + 1):
            count = 0
            curr = i
            while sequence[curr : curr + len(word)] == word:
                curr += len(word)
                count += 1
            max_count = max(max_count, count)
        return max_count


cases = [
    ("ababc", "ab", 2),
    ("ababc", "ba", 1),
    ("ababc", "ac", 0),
    ("aaabaaaabaaaabaaaaba", "aaaba", 4),
    ("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba", 5),
]

sol = Solution()
for (seq, word, exp) in cases:
    assert (
        got := sol.maxRepeating(seq, word)
    ) == exp, f"Failed case ({seq}, {word}) - expecting {exp}, got {got}"
