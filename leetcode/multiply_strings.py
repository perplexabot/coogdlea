"""Given two non-negative integers num1 and num2 represented as strings, return the product of num1
and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        converter = {str(x): x for x in range(10)}
        int_nums = []
        for char_number in [num1, num2]:
            curr_num = 0
            for char_digit in char_number:
                curr_num *= 10
                curr_num += converter[char_digit]
            int_nums.append(curr_num)
        return str(int_nums[0] * int_nums[1])


sol = Solution()

for x, y in [('2', '3'), ('123', '456')]:
    ans = sol.multiply(x, y)
    print(f"'{x}' * '{y}' = ", ans)
