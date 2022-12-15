"""
Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.
    For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

Example 1:
    Input: s = "1101"
    Output: true
    Explanation:
    The longest contiguous segment of 1s has length 2: "1101"
    The longest contiguous segment of 0s has length 1: "1101"
    The segment of 1s is longer, so return true.

Example 2:
    Input: s = "111000"
    Output: false
    Explanation:
    The longest contiguous segment of 1s has length 3: "111000"
    The longest contiguous segment of 0s has length 3: "111000"
    The segment of 1s is not longer, so return false.

Example 3:
    Input: s = "110100010"
    Output: false
    Explanation:
    The longest contiguous segment of 1s has length 2: "110100010"
    The longest contiguous segment of 0s has length 3: "110100010"
    The segment of 1s is not longer, so return false.

Constraints:
    1 <= s.length <= 100
    s[i] is either '0' or '1'.

---

A:
    len(s) < 1 ?
    s contains things other than 0 or 1?
    what if longest 1 is equal to longest 0?
    no zeros -> longest zero size = 0 (same with 1)

D:
    z_c = 0
    o_c = 0
    z_max = 0
    o_max = 0
    str:    110100010
    ind:    012345678
        0 -> o_c += 1 = 1
        1 -> o_c += 1 = 2
        2 -> o_max = max(o_c, o_max), o_c = 0, z_c += 1 = 1
        3 -> z_max = max(z_c, z_max), z_c = 0, o_c += 1 = 1
        4 -> o_max = max(o_c, o_max), o_c = 0, z_c += 1 = 1
        5 -> o_

P:
    for elem in s:
        if diff from previous elem:
            save current count
            restart stats
        else:
            increment
    return o_max > z_max
"""


def seq_check(s: str) -> bool:
    from itertools import groupby

    ans = groupby(s)
    maxes = {'1': 0, '0': 0}
    for e, seq in ans:
        maxes[e] = max(maxes[e], len([x for x in seq]))

    return maxes['0'] < maxes['1']


def seq_check_again(s: str) -> bool:
    if not s:
        return False

    prev = s[0]
    cnt = 1
    maxes = {'0': 0, '1': 1, 'x': float('-inf')}
    for e in s[1:] + 'x':
        if e == prev:
            cnt += 1
        else:
            maxes[prev] = max(maxes[prev], cnt)
            cnt = 1
            prev = e
    return maxes['1'] > maxes['0']


cases = [
    ('1101', True),
    ('', False),
    ('0', False),
    ('1', True),
    ('111000', False),
    ('110100010', False),
    ('01111110', True),
]

for s, exp in cases:
    assert (ans := seq_check_again(s)) == exp, f'Woops failed test case {s} - got {ans}'
