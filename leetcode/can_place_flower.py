"""
You have a long flowerbed in which some of the plots are planted, and some are not. However,
    flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
    and an integer n, return if n new flowers can be planted in the flowerbed without violating
    the no-adjacent-flowers rule.

Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

Constraints:
    1 <= flowerbed.length <= 2 * 10^4
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length

A:
    empty list -> true if n = 0
    list of size 1 -> true if list has a 0 else false
    n = 0 -> true

D:
    [1,0,0,0,1]
    [1,0,1,0,1] = 3
    3 > 1 -> true

P:
    potential = 0
    for i in range(len(flowerbed)):
        if spot == 1:
            continue

        prev = spot[i-1] if i else None
        next = spot[i+1] if i < len(flowerbed) else None
        if prev != 1 and next != 1:
            potential += 1
    return potential
"""


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    fb = flowerbed[:]
    for i in range(len(fb)):
        if fb[i] == 1:
            continue

        prv = fb[i - 1] if i else None
        nxt = fb[i + 1] if i + 1 < len(fb) else None

        if prv != 1 and nxt != 1:
            fb[i] = 1
    return fb.count(1) - flowerbed.count(1) >= n


cases = [
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),
    ([], 1, False),
    ([1], 1, False),
    ([0], 1, True),
    ([0, 1], 1, False),
    ([0, 1], 4, False),
    ([1, 0], 1, False),
    ([1, 0], 0, True),
    ([0, 1, 0], 1, False),
    ([0, 1, 0], 0, True),
    ([1, 0, 1], 1, False),
    ([1, 0, 1], 0, True),
    ([1, 0, 1], 10, False),
    ([0, 0], 1, True),
    ([0, 0], 2, False),
    ([0, 0, 0], 1, True),
    ([0, 0, 0], 2, True),
    ([0, 0, 0], 3, False),
]

for (flowerbed, n, exp) in cases:
    assert (
        got := canPlaceFlowers(flowerbed, n)
    ) == exp, f"Failed ({flowerbed}, {n}) - expecting ({exp}), got ({got})"
