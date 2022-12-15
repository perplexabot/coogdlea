"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4**x.

Example 1:
    Input: n = 16
    Output: true

Example 2:
    Input: n = 5
    Output: false

Example 3:
    Input: n = 1
    Output: true

Constraints:
    -2**31 <= n <= 2**31 - 1

Follow up: Could you solve it without loops/recursion?

A:
    n is negative   -> return false
    n is zero       -> return true
    n is not an int -> return false

D:
    16 -> ans = 16 ** (1/4)
        return ans == int(ans)
"""


def isPowerOfFour(n: int) -> bool:
    import math

    if n <= 0:
        return False
    ans = math.log(n) / math.log(4)
    return int(ans) == ans


cases = [
    (16, True),
    (5, False),
    (1, True),
    (0, False),
    (-1, False),
    (4, True),
    (-4, False),
    (625, False),
]

for (n, exp) in cases:
    assert (ans := isPowerOfFour(n)) == exp, f"Failed ({n}) - expecting ({exp}), got ({ans})"
