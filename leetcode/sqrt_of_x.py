"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
    The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator. For example, do not use
    pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
    0 <= x <= 2**31 - 1

A:
    x = 0 ->    0
    x < 0 ->    return None

D:
    sqrt(81)
        81 // 2 = 40
        40 * 40 > 81
        40 // 2 = 20
        20 * 20 > 81
        20 // 2 = 10
        10 * 10 > 81
        10 // 2 = 5
        5 * 5 < 81
        (10-5)//2 + 5 = 7
        7 * 7 < 81
        (10-7)//2 + 7 = 8
        8 * 8 < 81
        (10-8)//2 + 8 = 9
        9 * 8 == 81
        DONE
"""


def mySqrt(x: int) -> int:
    def binSearch(x, start, end):
        mid = ((end - start) // 2) + start
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        if mid * mid < x:
            return binSearch(x, mid, end)
        else:
            return binSearch(x, start, mid)

    return binSearch(x, 0, x) // 1 if x > 1 else x


cases = [
    (4, 2),
    (8, 2),
    (0, 0),
    (81, 9),
    (144, 12),
    (9, 3),
    (1, 1),
    (2, 1),
    (100, 10),
    (101, 10),
    (99, 9),
]

for (x, exp) in cases:
    assert (ans := mySqrt(x)) == exp, f"Failed with ({x}) - expecting ({exp}), got ({ans})"
