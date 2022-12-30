"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if
    either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be
    equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is
    equivalent to dominoes[j].

Example 1:
    Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
    Output: 1

Example 2:
    Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    Output: 3

Constraints:
    1 <= dominoes.length <= 4 * 10**4
    dominoes[i].length == 2
    1 <= dominoes[i][j] <= 9

A:
    empty list -> return 0
    no similars -> return 0

P:
    create counter
    for each key
        tote = keycnt + mirrkeycnt
        sum += tote if tote > 1 else 0
    return sum

"""


def numEquivDominoPairs(dominoes: list[list[int]]) -> int:
    from collections import defaultdict
    from math import comb

    cnts = defaultdict(int)
    for d in dominoes:
        tup = tuple(d)
        if tup in cnts:
            cnts[tup] += 1
        elif tup[::-1] in cnts:
            cnts[tup[::-1]] += 1
        else:
            cnts[tup] = 1

    return sum(comb(cnt, 2) for cnt in cnts.values())


cases = [([[1, 2], [2, 1], [3, 4], [5, 6]], 1), ([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]], 3)]

for (doms, exp) in cases:
    assert (
        got := numEquivDominoPairs(doms)
    ) == exp, f"Failed case ({doms}) - expecting ({exp}), got ({got})"
