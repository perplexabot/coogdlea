"""
Reversing an integer means to reverse all its digits.

    For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.

Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

Example 1:
    Input: num = 526
    Output: true
    Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

Example 2:
    Input: num = 1800
    Output: false
    Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.

Example 3:
    Input: num = 0
    Output: true
    Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.

Constraints:
    0 <= num <= 10^6

A:
    if num is empty -> return true
    if num contains non ints -> return false
    if num == 0 or 0000 or 000... return true
A:
    ?
D:
    1800
    0018 -> 18
    81
    1800 != 18 -> False
P:
    snum = str(num)
    rev1 = int(snum[::-1])
    snum = str(rev1)
    rev2 = int(snum[::-1])
    return num == rev2

O:
    possibly reverse int via loop and math (vs str casting)
"""


def isSameAfterReversals(num: int) -> bool:
    # snum = str(num)
    # rev1 = int(snum[::-1])
    # snum = str(rev1)
    # rev2 = int(snum[::-1])
    # return num == rev2
    return True if num == 0 else (not str(num).endswith('0') and not str(num).startswith('0'))


cases = [
    (526, True),
    (1800, False),
    (0, True),
    (000, True),
    (10, False),
    (1, True),
    (111, True),
]

for num, exp in cases:
    assert (
        ans := isSameAfterReversals(num)
    ) == exp, f"Failed case ({num}) - got ({ans}), expecting ({exp})"
