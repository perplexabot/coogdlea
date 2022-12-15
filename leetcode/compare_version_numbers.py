"""Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth
second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For
example, version number 3.4 has a revision number of 3 and 4 for its first and second level
revision number. Its third and fourth level revision number are both 0.



Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

Example 4:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”

Example 5:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its
third level revision number is default to "0"


Note:
Version strings are composed of numeric strings separated by dots . and this numeric strings may
have leading zeroes.

Version strings do not start or end with dots, and they will not be two consecutive dots.
"""


class Solution:
    from itertools import zip_longest as zpl

    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':
        version1_nums = version1.split('.')
        version1_nums = [int(x) for x in version1_nums]
        version2_nums = version2.split('.')
        version2_nums = [int(x) for x in version2_nums]

        for v1, v2 in self.zpl(version1_nums, version2_nums, fillvalue=0):
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0


inps = [
    ('0.1', '1.1', -1),
    ('1.0.1', '1', 1),
    ('7.5.2.4', '7.5.3', -1),
    ('1.01', '1.001', 0),
    ('1.0', '1.0.0', 0),
    ('0', '00', 0),
    ('01', '0001', 0),
    ('0.1', '0.1', 0),
    ('1.2.3.4.5', '1.2.3.4.5', 0),
    ('1.2.3.4.6', '1.2.3.4.5', 1),
    ('1.2.3.4.5', '1.2.3.4.6', -1),
    ('1.2.3.4.5', '2.2.3.4.5', -1),
]

sol = Solution()
for v1, v2, exp in inps:
    print(f"Comparing {v1} and {v2} and asserting...")
    assert exp == sol.compareVersion(v1, v2)
