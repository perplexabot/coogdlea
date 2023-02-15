"""
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the
    binary representation of n. If there are no two adjacent 1's, return 0.
Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between
    two 1's is the absolute difference between their bit positions. For example, the two 1's
    in "1001" have a distance of 3.

Example 1:
    Input: n = 22
    Output: 2
    Explanation: 22 in binary is "10110".
    The first adjacent pair of 1's is "10110" with a distance of 2.
    The second adjacent pair of 1's is "10110" with a distance of 1.
    The answer is the largest of these two distances, which is 2.
    Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.

Example 2:
    Input: n = 8
    Output: 0
    Explanation: 8 in binary is "1000".
    There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

Example 3:
    Input: n = 5
    Output: 2
    Explanation: 5 in binary is "101".

Constraints:
    1 <= n <= 10**9

A:
    n = 0   -> not possible
    n binary has single 1 -> return 0
    n binary is 11  ->  return 1

D:
    Input: n = 22
    b = binary(22) = 0b10110 = "10110"

    if b.count(1) == 1:
        return 0

    start = b.find(1)

    max_count = float(-inf)
    for bin in b[start:]:
        if bin == 1:
            max_count = max(count, max_count)
        count += 1
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        binary = format(n, 'b')
        if binary.count('1') == 1:
            return 0

        start = binary.find('1')
        max_count = float('-inf')
        count = 0
        for b in binary[start:]:
            if b == '1':
                max_count = max(count, max_count)
                count = 0
            count += 1

        return max_count


cases = [(22, 2), (8, 0), (5, 2)]

sol = Solution()
for (n, exp) in cases:
    assert (got := sol.binaryGap(n)) == exp, f"Failed case ({n}) - expecting ({exp}), got ({got})."
