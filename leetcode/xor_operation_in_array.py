"""
You are given an integer n and an integer start.
Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.

Example 1:
    Input: n = 5, start = 0
    Output: 8
    Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
    Where "^" corresponds to bitwise XOR operator.

Example 2:
    Input: n = 4, start = 3
    Output: 8
    Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.

Constraints:
    1 <= n <= 1000
    0 <= start <= 1000
    n == nums.length

A:
    start is negative?  -> constraint says not possible
    n is negative?      -> constraint says not possible
    n i zero            -> constraint says not possible

D:
    Input: n = 5, start = 0
    array = [(0 + 2*0), (0 + 2*1), (0 + 2*2), (0 + 2*3), (0 + 2*4)] = [0, 2, 4, 6, 8]
    xor = 0 ^ 2 ^ 4 ^ 6 ^ 8 = int(1000, 2)
"""


def xorOperation(n: int, start: int) -> int:
    from functools import reduce

    if n <= 0 or start < 0:
        return None

    return reduce(lambda x, y: x ^ y, [start + (2 * i) for i in range(n)])


cases = [(5, 0, 8), (4, 3, 8), (0, 10, None), (10, -1, None)]

for (n, start, exp) in cases:
    assert (
        got := xorOperation(n, start)
    ) == exp, f"Failed case ({n}, {start}) - expecting ({exp}), got ({got})"
