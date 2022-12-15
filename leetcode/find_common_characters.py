"""
Given a string array `words`, return an array of all characters that show up in all strings within
    the words (including duplicates). You may return the answer in any order.

Example 1:
    Input: words = ["bella","label","roller"]
    Output: ["e","l","l"]

Example 2:
    Input: words = ["cool","lock","cook"]
    Output: ["c","o"]

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.

A:
    words is empty -> return empty list
    words contains things other than string -> ignore none string
    no char is in all the words -> empty list
    words assumed to be lowercase
    a word is an empty string

D:
    use bella:
        b -> cnts[b] = [1,1,0]
        e -> cnts[e] = [1,1,1]
        l -> cnts[l] = [2,2,2]
        l -> cnts[l] = [2,2,2]
        a -> cnts[a] = [1,1,0]

    for c in cnts:
        if 0 no in cnts[c]:
            times = min(cnts[c])
            ans.extend(c for i in range(times))

P:
    if not words:
        return []

    for c in words[0]:
        counts[c] = [s.count[c] for s in words]

    for char in counts:
        if 0 not in counts[char]:
            ans.extend(char * min(counts[char]))
    return ans
"""


def commonChars(words: list[str]) -> list[str]:
    if not words:
        return []

    counts = {char: [s.count(char) for s in words] for char in words[0]}

    ans = []
    for char in counts:
        if 0 not in counts[char]:
            ans.extend(char for i in range(min(counts[char])))

    return ans


cases = [
    (["bella", "label", "roller"], ["e", "l", "l"]),
    (["a", "b", "c"], []),
    (["aaa", "aa", "a"], ["a"]),
    (["cool", "lock", "cook"], ["c", "o"]),
    ([], []),
    ([""], []),
    (["", ""], []),
    (["a", ""], []),
]

for words, exp in cases:
    assert (ans := commonChars(words)) == exp, f"Woops failed {words} - got {ans} instead of {exp}"
