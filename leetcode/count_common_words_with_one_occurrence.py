"""
Given two string arrays words1 and words2, return the number of strings that appear exactly
    once in each of the two arrays.

Example 1:
    Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
    Output: 2
    Explanation:
    - "leetcode" appears exactly once in each of the two arrays. We count this string.
    - "amazing" appears exactly once in each of the two arrays. We count this string.
    - "is" appears in each of the two arrays, but there are 2 occurrences of it in
        words1. We do not count this string.
    - "as" appears once in words1, but does not appear in words2. We do not count this string.
    Thus, there are 2 strings that appear exactly once in each of the two arrays.

Example 2:
    Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
    Output: 0
    Explanation: There are no strings that appear in each of the two arrays.

Example 3:
    Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
    Output: 1
    Explanation: The only string that appears exactly once in each of the two arrays is "ab".

Constraints:
    1 <= words1.length, words2.length <= 1000
    1 <= words1[i].length, words2[j].length <= 30
    words1[i] and words2[j] consists only of lowercase English letters.

A:
    what if at least one list is empty      ->  return 0
    what if at least one list is none       ->  return 0

D:
    counts1 = Count(words1)
    counts2 = Count(words2)
    return len([k for k in counts1 if k in counts2 and counts2[k] == 1 and counts1[k] == 1])
"""


def countWords(words1: list[str], words2: list[str]) -> int:
    from collections import Counter

    if not words1 or not words2:
        return 0

    counts1 = Counter(words1)
    counts2 = Counter(words2)

    return len([k for k in counts1 if k in counts2 and counts2[k] == 1 and counts1[k] == 1])


cases = [
    (["b", "bb", "bbb"], ["a", "aa", "aaa"], 0),
    (["a", "ab"], ["a", "a", "a", "ab"], 1),
    (None, ["a"], 0),
    ([], [], 0),
    (["a"], ["b"], 0),
    (["b"], ["b"], 1),
]

for (words1, words2, exp) in cases:
    assert (
        ans := countWords(words1, words2)
    ) == exp, f"Failed ({words1}, {words2}) - expecting ({exp}), got ({ans})"
