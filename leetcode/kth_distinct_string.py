"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present
    in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

Example 1:
    Input: arr = ["d","b","c","b","c","a"], k = 2
    Output: "a"
    Explanation:
    The only distinct strings in arr are "d" and "a".
    "d" appears 1st, so it is the 1st distinct string.
    "a" appears 2nd, so it is the 2nd distinct string.
    Since k == 2, "a" is returned.

Example 2:
    Input: arr = ["aaa","aa","a"], k = 1
    Output: "aaa"
    Explanation:
    All strings in arr are distinct, so the 1st string "aaa" is returned.

Example 3:
    Input: arr = ["a","b","a"], k = 3
    Output: ""
    Explanation:
    The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".

Constraints:
    1 <= k <= arr.length <= 1000
    1 <= arr[i].length <= 5
    arr[i] consists of lowercase English letters.

A:
    empty list -> return ""
    list with no distincts -> return ""
    k is not a number -> return ""
    k is larger than len(arr) -> return ""
    k is larger than unique cnt -> return ""
    arr contains something other than string -> constraint says not possible
    assuming python3.7 so that we can assume dict keys are ordered (no need for ordereddict)

A:
    ?
D:
    cnts['d'] = 1
    cnts['b'] = 1
    cnts['c'] = 1
    cnts['b'] = 2
    cnts['c'] = 2
    cnts['a'] = 1
    -> cnts = {'d':1, 'b': 2, 'c':2, 'a':1}

    uniques = {'d':1, 'a':1}
    kth_key = uniques.keys()[k]
    return uniques[kth_key]
P:
    if not arr or k > len(arr):
        return ""

    dict = {}
    for s in arr:
        dict[s] += 1

    uniques = {k:v for k,v in cnts.items() if v == 1}
    if k > len(uniques):
        return ""

    kth_key = uniques.keys()[k]
    return uniques[kth_key]
"""


def kthDistinct(arr: list[str], k: int) -> str:
    if not arr or k > len(arr):
        return ""

    from collections import defaultdict

    d = defaultdict(int)
    for s in arr:
        d[s] += 1

    uniques = {k: v for k, v in d.items() if v == 1}
    if k > len(uniques):
        return ""

    kth_key = list(uniques.keys())[k - 1]
    return kth_key


cases = [
    (["d", "b", "c", "b", "c", "a"], 2, "a"),
    (["aaa", "aa", "a"], 1, "aaa"),
    (["a", "b", "a"], 3, ""),
    ([], 10, ""),
    (["a"], 10, ""),
    (["a", "b", "c", "d"], 1, "a"),
    (["a", "b", "c", "d"], 2, "b"),
    (["a", "b", "c", "d"], 3, "c"),
    (["a", "b", "c", "d"], 4, "d"),
    (["a", "b", "c", "d"], 5, ""),
]

for (arr, k, exp) in cases:
    assert (
        ans := kthDistinct(arr, k)
    ) == exp, f"Failed with ({arr}, {k}) - got ({ans}), expecting ({exp})"
