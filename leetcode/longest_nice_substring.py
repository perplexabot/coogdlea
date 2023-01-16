"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in
    uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B'
    and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
Given a string s, return the longest substring of s that is nice. If there are multiple, return the
    substring of the earliest occurrence. If there are none, return an empty string.

Example 1:
    Input: s = "YazaAay"
    Output: "aAa"
    Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and
        both 'A' and 'a' appear.
    "aAa" is the longest nice substring.

Example 2:
    Input: s = "Bb"
    Output: "Bb"
    Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a
        substring.

Example 3:
    Input: s = "c"
    Output: ""
    Explanation: There are no nice substrings.

Constraints:
    1 <= s.length <= 100
    s consists of uppercase and lowercase English letters.

A:
    s = ""  ->  return ""
    s contains none alpha   ->   not possible
    s of size 1 -> return ""
    uniques is odd -> return false
    uniques is even -> could be nice
    which to return if multiple?    ->  first occurrence

D:
    Input: s = "YazaAay"
    is YazaAay nice? no
        is YazaAa nice? no
            is YazaA nice? no
                is Yaza nice? no
                    is Yaz nice? no
                    is aza nice? no
                is azaA nice? no
                    is aza nice? no
                    is zaA nice? no
            is azaAa nice?
                is azaA nice? no
                    is aza nice? no
                    is zAa nice? no
                is zaAa nice? no
                    is zaA nice? no
                    is aAa nice? yes return
        is azaAay nice?
            is azaAa nice?
                is azaA nice? no
                is zaAa nice? no
            is zaAay nice?

O:
    This method doesn't meet time requirements. The last case below takes a lifetime and a half to finish. A quicker method
    of splitting string on letter that doesn't have a lower/upper pair is a better approach - not implemented

"""


def longestNiceSubstring(s: str) -> str:
    from collections import Counter

    if len(s) < 2:
        return ""

    notNice = set()

    def isNice(s, start, end):
        if end == start:
            return ""
        if (start, end) in notNice:
            s0 = isNice(s, start, end - 1)
            s1 = isNice(s, start + 1, end)
            return s0 if len(s0) >= len(s1) else s1
        else:
            cnts = Counter(s[start : end + 1])
            for c in s[start : end + 1]:
                if cnts[c.lower()] > 0 and cnts[c.upper()] > 0:
                    continue
                else:
                    notNice.add((start, end))
                    break
            else:
                return s[start : end + 1]

            s0 = isNice(s, start, end - 1)
            s1 = isNice(s, start + 1, end)
            return s0 if len(s0) >= len(s1) else s1

    return isNice(s, 0, len(s))


cases = [
    ("YazaAay", "aAa"),
    ("Bb", "Bb"),
    ("c", ""),
    ("", ""),
    ("azz", ""),
    ("aZz", "Zz"),
    ("aAbcC", "aA"),
    ("aabcCccc", "cCccc"),
    ("abCcccCBA", "abCcccCBA"),
    # ("xLeElzxgHzcWslEdgMGwEOZCXwwDMwcEhgJHLL", ""),
]

for (case, exp) in cases:
    assert (
        got := longestNiceSubstring(case)
    ) == exp, f"Failed case ({case}) - got ({got}), expecting ({exp})"
