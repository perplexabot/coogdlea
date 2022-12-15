"""
Given an integer num, repeatedly add all its digits until the result has only one digit,
    and return it.

Example 1:
    Input: num = 38
    Output: 2
    Explanation: The process is
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2
    Since 2 has only one digit, return it.

Example 2:
    Input: num = 0
    Output: 0

Constraints:
    0 <= num <= 2**31 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?

A:
    if num is empty -> return 0
    if num is str -> cast to int

A:
    ?

D:
    sum = 0
    12345
    sum += 5 = 5
    1234
    sum += 4 = 9
    123
    sum += 3 = 12
    12
    sum += 2 = 14
    1
    sum += 1 = 15

    sum = 0
    15
    sum += 5 = 5
    1
    sum += 1 = 6

P:
    digits = [*str(num)]
    if len(digits) == 1:
        return int(digits[0])

    while len(digits) > 1:
        sum = sum([int(x) for x in digits])
        digits = [*str(sum)]

    return digits[0]

O:
    - could use math (mod and division) to grab elements from int (with no casting)
"""


def addDigits(num: int) -> int:
    if not num:
        return 0

    digits = [*str(num)]

    while len(digits) > 1:
        s = sum([int(x) for x in digits])
        digits = [*str(s)]

    return int(digits[0])


cases = [(38, 2), (0, 0), ('', 0), (None, 0), (12345, 6), (1, 1), (11, 2), (1000, 1), (9, 9)]

for (num, exp) in cases:
    assert (ans := addDigits(num)) == exp, f"Failed with ({num}) - got ({ans}), expecting ({exp})"
