"""Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        from string import ascii_uppercase

        conv = {ind + 1: c for ind, c in enumerate(ascii_uppercase)}

        s = ''
        curr = n
        while curr:
            rem = (curr % 26) or 26
            s = ''.join([conv[rem], s])
            curr = (curr - rem) // 26
        return s


sol = Solution()
for i in range(26 * 2 + 1):
    print(f"Doing {i}, got {sol.convertToTitle(i)}")

print(f"Doing 701, got {sol.convertToTitle(701)}")
print(f"Doing 702, got {sol.convertToTitle(702)}")
print(f"Doing 582, got {sol.convertToTitle(582)}")
