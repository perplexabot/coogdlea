"""Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


inps = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ('1,2,3,2,1', True),
    ('1,2,2,1', True),
    ('1,2,3,1', False),
    ('1', True),
    ('', True),
    ('aba aba', True),
]

sol = Solution()

for inp, exp in inps:
    print(f'isPalindroming "{inp}" and asserting...')
    assert exp == sol.isPalindrome(inp)
