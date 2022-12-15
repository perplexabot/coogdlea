"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.
 
Example 1:
    Input: num = 16
    Output: true

Example 2:
    Input: num = 14
    Output: false

Constraints:
    1 <= num <= 2^31 - 1

A:
    num is 0    -> return true
    num is < 0  -> not possible according to constraint

D:
    16
    ((16-0)//2) + 0 = 8, 8*8 > 16
    ((8-0)//2) + 0 = 4, 4*4 == 16
    true

    145
    s=0,e=145,  ((145-0)//2) + 0 = 72, 72*72 > 145
    s=0,e=72    ((72-0)//2) + 0 = 36, 36*36 > 145
    s=0,e=36    ((36-0)//2) + 0 = 18, 18*18 > 145
    s=0,e=18    ((18-0)//2) + 0 = 9, 9*9 < 145
    s=9,e=18    ((18-9)//2) + 8 = 12, 12*12 < 145 && (12+1)(12+1) > 145
    false
"""


def isPerfectSquare(num: int) -> bool:
    def binSearch(s, e, val):
        m = ((e - s) // 2) + s
        if m * m == num:
            return True
        if m * m < val < (m + 1) * (m + 1):
            return False

        if m * m < val:
            return binSearch(m, e, val)
        else:
            return binSearch(s, m, val)

    return binSearch(0, num, num) if num > 1 else True


cases = [
    (16, True),
    (14, False),
    (145, False),
    (144, True),
    (0, True),
    (1, True),
    (2, False),
    (4, True),
    (9, True),
    (36, True),
    (100, True),
    (101, False),
]

for (num, exp) in cases:
    assert (got := isPerfectSquare(num)) == exp, f"Failed ({num}) - expecting ({exp}), got ({got})"
