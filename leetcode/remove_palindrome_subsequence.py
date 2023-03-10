"""
Given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one
palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string, if it is generated by deleting some characters of a
given string without changing its order.

A string is called palindrome if is one that reads the same backward as well as forward.

Example 1:
    Input: s = "ababa"
    Output: 1
    Explanation: String is already palindrome
Example 2:
    Input: s = "abb"
    Output: 2
    Explanation: "abb" -> "bb" -> "".
    Remove palindromic subsequence "a" then "bb".
Example 3:
    Input: s = "baabb"
    Output: 2
    Explanation: "baabb" -> "b" -> "".
    Remove palindromic subsequence "baab" then "b".
Example 4:
    Input: s = ""
    Output: 0

Constraints:
    0 <= s.length <= 1000
    s only consists of letters 'a' and 'b'

URL: https://leetcode.com/problems/remove-palindromic-subsequences/

"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0

        if self.isPalindrome(s):
            return 1

        def pal_split(s: str, cnt: int) -> int:
            if len(s) < 2:
                return cnt + 1

            for pivot in range(1, len(s)):
                left_is_p = self.isPalindrome(s[:pivot])
                right_is_p = self.isPalindrome(s[pivot:])
                if left_is_p:
                    P = pivot

                if left_is_p and right_is_p:
                    return cnt + 2

            return pal_split(s[P:], cnt + 1)

        return pal_split(s, 0)

    def isPalindrome(self, s: str) -> bool:
        p = len(s) // 2
        if len(s) % 2:
            xl = p - 1
            xr = p + 1
        else:
            xl = p - 1
            xr = p

        while xl >= 0:
            if s[xl] != s[xr]:
                return False
            xl -= 1
            xr += 1
        return True


pal_inps = [
    ('a', True),
    ('', True),
    ('ab', False),
    ('aa', True),
    ('aba', True),
    ('aab', False),
    ('aabb', False),
    ('aabbaa', True),
]

pal_sub_inps = [
    ("", 0),
    ("a", 1),
    ("aa", 1),
    ("ab", 2),
    ("aba", 1),
    ("baabb", 2),
    ("abb", 2),
    ("ababa", 1),
    ("bbbabb", 2),
    ("bbbbab", 2),
    ("bababa", 2),
    ("babbb", 2),
    ("abbabbbaa", 3),
    ("bbaabaaa", 2),
]

sol = Solution()
for inp, exp in pal_inps:
    assert (got := sol.isPalindrome(inp)) == exp, f"Failed on {inp}, expecting {exp}, got {got}"

for inp, exp in pal_sub_inps:
    print(f'----> {inp}')
    assert (got := sol.removePalindromeSub(inp)) == exp, f"Failed: expecting {exp}, got {got}"
    print('PASS')
