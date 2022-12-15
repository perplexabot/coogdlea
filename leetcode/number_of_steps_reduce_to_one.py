"""
Given a number s in their binary representation. Return the number of steps to reduce it to 1 under the following rules:
    If the current number is even, you have to divide it by 2.
    If the current number is odd, you have to add 1 to it.
It's guaranteed that you can always reach to one for all testcases.

Example 1:
    Input: s = "1101"
    Output: 6
    Explanation: "1101" corressponds to number 13 in their decimal representation.
    Step 1) 13 is odd, add 1 and obtain 14.
    Step 2) 14 is even, divide by 2 and obtain 7.
    Step 3) 7 is odd, add 1 and obtain 8.
    Step 4) 8 is even, divide by 2 and obtain 4.
    Step 5) 4 is even, divide by 2 and obtain 2.
    Step 6) 2 is even, divide by 2 and obtain 1.

Example 2:
    Input: s = "10"
    Output: 1
    Explanation: "10" corressponds to number 2 in their decimal representation.
    Step 1) 2 is even, divide by 2 and obtain 1.

Example 3:
    Input: s = "1"
    Output: 0


Constraints:
    1 <= s.length <= 500
    s consists of characters '0' or '1'
    s[0] == '1'

URL:
    https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
"""

# A Are numbers all positive?
#   Max binary size?
#   Can s = "" or None or something?
#   Case where s == "1"
#   Case where s == "0"
#   Take care of the carry! (e.g: 1111)
#   Need to take care of cases like: 00001
# D 1100101001
#   1100101010
#   0110010101
#   0110010110
#   0011001011
#   0011001100
#   0001100110
#   0000110011
#   0000110100
#   0000011010
#   0000001101
#   0000001110
#   0000000111
#   0000001000
#   0000000100
#   0000000010
#   0000000001
# P if s == 1, return 1
#   steps = 0
#   while s != 1:
#       if S%2 == 1:
#           s += 1
#           steps += 1
#       else:
#           s /= 2
#           steps += 1
#
# O keep track of indices rather than creating a new string every iteration


class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        new_s = int(s, 2)
        while new_s != 1:
            new_s = new_s + 1 if new_s & 1 else new_s // 2
            steps += 1
        return steps


inps = [('1101', 6), ('10', 1), ('1', 0), ('00001', 0), ('1110', 5)]

sol = Solution()
for inp, exp in inps:
    print(f'Doing {inp}')
    ans = sol.numSteps(inp)
    assert ans == exp, f"Failed! input: {inp}   output: {ans}   expected: {exp}"
