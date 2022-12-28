"""
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to
    gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes
    her candies very much, and she wants to eat the maximum number of different types of candies
    while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of
    candies she can eat if she only eats n / 2 of them.

Example 1:
    Input: candyType = [1,1,2,2,3,3]
    Output: 3
    Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat
        one of each type.

Example 2:
    Input: candyType = [1,1,2,3]
    Output: 2
    Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3],
        or [2,3], she still can only eat 2 different types.

Example 3:
    Input: candyType = [6,6,6,6]
    Output: 1
    Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only
        has 1 type.

Constraints:
    n == candyType.length
    2 <= n <= 10**4
    n is even.
    -10**5 <= candyType[i] <= 10**5

A:
    candyType is empty         ->  return 0
    candyType has one type     ->  return 1
    candyType only has uniques ->  return n//2
    candyType uniques < n//2   ->  return number of uniques
    candyType uniques >= n//2  ->  n//2

D:
    Input: candyType = [1,1,2,2,3,3]
    uniqes = {1,2,3}
    l = len(uniques) == 3
    h = len(candyType) // 2
    return 2 (since l >= h)
"""


def distributeCandies(candyType: list[int]) -> int:
    if not candyType:
        return 0

    half = len(candyType) // 2
    uniques = len(set(candyType))

    return half if uniques >= half else uniques


cases = [
    ([1, 1, 2, 2, 3, 3], 3),
    ([1, 1, 2, 3], 2),
    ([6, 6, 6, 6], 1),
    ([], 0),
    ([1, 2, 3, 4], 2),
    ([1, 2], 1),
    ([1, 1], 1),
]

for (candyType, exp) in cases:
    assert (
        got := distributeCandies(candyType)
    ) == exp, f"Failed case ({candyType}) - expecting ({exp}), got ({got})"
