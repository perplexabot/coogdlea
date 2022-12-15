"""
You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
    Input: s = "(abcd)"
    Output: "dcba"

Example 2:
    Input: s = "(u(love)i)"
    Output: "iloveu"
    Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
    Input: s = "(ed(et(oc))el)"
    Output: "leetcode"
    Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Example 4:
    Input: s = "a(bcdefghijkl(mno)p)q"
    Output: "apmnolkjihgfedcbq"

Constraints:
    0 <= s.length <= 2000
    s only contains lower case English characters and parentheses.
    It's guaranteed that all parentheses are balanced.

URL: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
"""

# AADPOCT!
# A:    can s be empty? Yes, according to the constraints.
#       does every paran have a matching pair? Yes, according to the constraints.
#       what to do in a case with n consecutive parenths? e.g: ((hello)). Just reverse twice.
#           in this case you can just count the parenths on one side and depending if cnt is
#           odd/even, act accordingly.
# A:    What to do in the case of something like (a(b(c(def)))). Can still use odd/even technique?
# D:    (a(b(c(def)))):
#           (a(b(cfed)))
#           (a(bdefc))
#           (acfedb)
#           bdefca
# P:    def main (s):
#           if '(' not in s:
#               return s
#           else:
#               (l,r) = find_inner_str(s)
#               r = reverse(s[l:r])
#               main(s[:l] + r + s[r:])
#
#       def find_inner_str(s):
#           return (s.rfind('(')+1, s.find(')'))
#
#       Recurrence relation
#           Assume that n here is the parenthesis pair count, I know, that is quite the assumption
#           General relation: T(n) = T(n-1) + O(n)
#           Base relation (for n = 0): T(0) = O(1)
#
#           T(n)_= T(n-1) + n and T(1) = 1
#           T(n-1) = T(n-2) + (n-1)
#           T(n-2) = T(n-3) + (n-2)
#           T(n-3) = T(n-4) + (n-3)
#           Subbing the above equations
#               T(n) = T(n-2) + (n-1) + n                   = T(n-2) + 2n - 1 = T(n-2) + 2n - 2C0
#               T(n) = T(n-3) + (n-2) + (n-1) + n           = T(n-3) + 3n - 3 = T(n-3) + 3n - 3C1
#               T(n) = T(n-4) + (n-3) + (n-2) + (n-1) + n   = T(n-4) + 4n - 6 = T(n-4) + 4n - 4C2
#               .
#               .
#               .
#           A pattern can be seen
#               T(n) = T(n-k) + kn - kC(k-2) = T(n-k) +kn - k(k-1)/2
#
#           Using the base case to find k:
#               T(0) = T(n-k) => 0 = n-k => k = n
#
#           Subbing k back into pattern eq:
#               T(n) = T(0) + n^2 + n(n-1)/2 = O(1) + O(n^2) + m*O(n^2) = O(n^2)
#
#           This can be confirmed by comparing to any known algorithm with the same recurrence
#           relation, for example, selection sort.
# O:    One can pass the substring indices to find_inner_str() function.
#       A none recursive approach may be more efficient.
#       use a list (vs string) to reverse in place (join list upon return)


class Solution:
    def reverseParentheses(self, s: str) -> str:
        if '(' not in s:
            return s

        l = s.rfind('(')
        r = s.find(')', l)
        return self.reverseParentheses(s[0:l] + s[l + 1 : r][::-1] + s[r + 1 :])


inps = [
    ('', ''),
    ('hello', 'hello'),
    ('a', 'a'),
    ('(a)', 'a'),
    ('(((a)))', 'a'),
    ('(a(b(c(def))))', 'bdefca'),
    ('(abcd)', 'dcba'),
    ('(u(love)i)', 'iloveu'),
    ('(ed(et(oc))el)', 'leetcode'),
    ('a(bcdefghijkl(mno)p)q', 'apmnolkjihgfedcbq'),
    ('a(b)c(d)', 'abcd'),
    ('a(bc)d(ef)', 'acbdfe'),
    ('a((bc)d)(ef)', 'adbcfe'),
]

sol = Solution()
for t, e in inps:
    print(f"Testing {t}, expecting {e}")
    ans = sol.reverseParentheses(t)
    assert ans == e, f"got: {ans}"
