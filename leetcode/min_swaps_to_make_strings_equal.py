"""
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only.
Your task is to make these two strings equal to each other.
You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].
Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

Example 1:
    Input: s1 = "xx", s2 = "yy"
    Output: 1
    Explanation:
    Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

    xx
    yy
    **

Example 2:
    Input: s1 = "xy", s2 = "yx"
    Output: 2
    Explanation:
    Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
    Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
    Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

Example 3:
    Input: s1 = "xx", s2 = "xy"
    Output: -1

Example 4:
    Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
    Output: 4


URL: https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
"""

# A:
#   Case where len(s1) == 0
#   Case where s1 == s2
# A:
#   If s1.count('x') + s2.count('x') not divisible by 2, then return -1
#   If s1.count('y') + s2.count('y') not divisible by 2, then return -1
#   Else figure out how many swaps
# D:
#   xxyyxyxyxx
#   xyyxyxxxyx
#    * *** **
#   xxyyxyxyyx
#   xxyxyxxxyx
#      *** *
#   xxyyxyxxyx
#   xxyyyxxxyx
#       **
#   xxyyyyxxyx
#   xxyyyxxxxx
#        *  *
#   xxyyyyxxxx
#   xxyyyyxxxx


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        if (s1.count('x') + s2.count('x')) % 2:
            return -1
        if (s1.count('y') + s2.count('y')) % 2:
            return -1

        swaps = 0
        oppo = {'x': 'y', 'y': 'x'}
        diff_inds = set(i for i in range(len(s1)) if s1[i] != s2[i])
        while diff_inds:
            d = diff_inds.pop()
            for i in diff_inds:
                if oppo[s1[d]] == s2[i]:
                    diff_inds.remove(i)
                    swaps += 1
                    break
            else:
                for i in diff_inds:
                    if oppo[s1[d]] == s1[i]:
                        diff_inds.remove(i)
                        swaps += 2
                        break
        return swaps


inps = [
    (('xx', 'yy'), 1),
    (('xy', 'yx'), 2),
    (('xx', 'xy'), -1),
    (('xxyyxyxyxx', 'xyyxyxxxyx'), 4),
    (('', ''), 0),
    (('xxx', 'yyy'), -1),
    (('x', 'y'), -1),
]

sol = Solution()
for inp, exp in inps:
    ans = sol.minimumSwap(*inp)
    assert ans == exp, f"Failed with {inp}. Got {ans}, expecting {exp}"
