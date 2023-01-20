"""
Given two non-negative integers low and high. Return the count of odd numbers between low and
    high (inclusive).

Example 1:
    Input: low = 3, high = 7
    Output: 3
    Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
    Input: low = 8, high = 10
    Output: 1
    Explanation: The odd numbers between 8 and 10 are [9].

Constraints:
    0 <= low <= high <= 10^9

A:
    l == h                          ->  return 1 if l is odd else 0
    l is even and h is even         ->  e.g: (2,3,4,5,6) -> (h - l)//2
    l is odd and h is odd           ->  e.g: (1,2,3,4,5,6,7,8,9) -> 2 + ((h - l)//2 - 1)
    l or h is odd and other even    ->  e.g: (1,2,3,4) -> 1 + ((h - l + 1)//2 - 1)

D:
    3,7
        both odd
            2 + ( (7-3)//2 - 1) = 2 + (2 - 1) = 3
    8,10
        both even
            (10 - 8)//2 = 2//2 = 1

    1,10
        one odd, one even
            1 + ( (10-1 + 1)//2 - 1) = 1 + (5 - 1) = 5
"""


def countOdds(low: int, high: int) -> int:
    if low % 2 and high % 2:
        return 2 + ((high - low) // 2 - 1)
    elif not low % 2 and not high % 2:
        return (high - low) // 2
    else:
        return (high - low + 1) // 2


cases = [(3, 7, 3), (8, 10, 1), (1, 10, 5), (1, 1, 1), (2, 2, 0), (1, 2, 1), (1, 3, 2), (2, 4, 1)]

for (low, high, exp) in cases:
    assert (
        got := countOdds(low, high)
    ) == exp, f"Failed case ({low}, {high}) - expecting ({exp}), got ({got})."
