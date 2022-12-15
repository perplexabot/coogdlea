"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end
    indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index.

Example 1:
    Input: s = "abbxxxxzzy"
    Output: [[3,6]]
    Explanation: "xxxx" is the only large group with start index 3 and end index 6.

Example 2:
    Input: s = "abc"
    Output: []
    Explanation: We have groups "a", "b", and "c", none of which are large groups.

Example 3:
    Input: s = "abcdddeeeeaabbbcd"
    Output: [[3,5],[6,9],[12,14]]
    Explanation: The large groups are "ddd", "eeee", and "bbb".

Constraints:
    1 <= s.length <= 1000
    s contains lowercase English letters only.

A:
    if s is empty? -> []
    is s has no large groups -> []
    multiple large groups with same char -> return both intervals
    if len(s) <  3 -> []
    if s contains none letter -> constraint says never happens (don't think about)
A:
    ?

D:
    str:    abbxxxxzyy
    ind:    0123456789

    0 -> start=0
    1 -> save([start=0, end=curr_ind-1=0]), start=curr_ind=1
    2 -> start=1
    3 -> save([start=1, end=curr_ind-1=2]), start=curr_ind=3
    4 -> start=3
    5 -> start=3
    6 -> start=3
    7 -> save([start=3, end=curr_ind-1=6]), start=curr_ind=7
    8 -> save([start=7, end=curr_ind-1=7]), start=curr_ind=8
    9 -> start=8

    save([start=8, end=len(s)-1)

    bounds = [0,0], [1,2], [3,6], [7,7], [8,9]
    big_bounds = [3,6]

P:
    if len(s) < 3:
        return []

    start=0
    curr=s[0]
    for c, ind in enumerate(s[1:]):
        if c != curr:
            bounds.append([start, ind-1])
            curr = c
            start = ind
    bounds.append([start, len(s) - 1])


    #abbbc
    #01234
    big_bounds = [x for x in bounds if x[1] - x[0] > 1]
"""


def largeGroupPositions(s: str) -> list[list[int]]:
    if len(s) < 3:
        return []

    start = 0
    curr = s[0]
    bounds = []

    for ind, c in enumerate(s[1:]):
        if c != curr:
            bounds.append([start, ind])
            curr = c
            start = ind + 1
    bounds.append([start, len(s) - 1])
    return [x for x in bounds if x[1] - x[0] > 1]


cases = [
    ("abbxxxxzzy", [[3, 6]]),
    ("abc", []),
    ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
    ("", []),
    ("a", []),
    ("aa", []),
    ("aaa", [[0, 2]]),
    ("abbc", []),
    ("abcdeee", [[4, 6]]),
    ("abcdeeefff", [[4, 6], [7, 9]]),
]

for s, exp in cases:
    assert (ans := largeGroupPositions(s)) == exp, f"Failed {s}. Expecting ({exp}) but got ({ans})"
