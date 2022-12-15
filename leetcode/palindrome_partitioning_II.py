"""Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        P = {(i, i): True for i in range(len(s))}
        C = {}

        for sz in range(2, len(s) + 1):
            for start in range(0, len(s) - sz + 1):
                i = start
                j = i + sz - 1

                if sz == 2:
                    P[(i, j)] = s[i] == s[j]
                else:
                    P[(i, j)] = P[(i + 1, j - 1)] and s[i] == s[j]

        for i in range(len(s)):
            if P[(0, i)]:
                C[i] = 0
            else:
                C[i] = float('inf')
                for j in range(i):
                    if P[(j + 1, i)]:
                        C[i] = min(C[i], 1 + C[j])
        return C[len(s) - 1]


inps = [
    "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp",
    "kwtbjmsjvbrwriqwxadwnufplszhqccayvdhhvscxjaqsrmrrqngmuvxnugdzjfxeihogzsdjtvdmkudckjoggltcuybddbjoizu",
    "ababababababababababababcbabababababababababababa",
    "ccaacabacb",
    "cabababcbc",
    'abcccb',
    'aab',
    'aba',
    'abaxyzaba',
    'abc',
    'a',
    '',
    'aaa',
    'aa',
    'ab',
    'abaabadefghabazzaba',
    'abaxyz',
    'xyzaba',
]
sol = Solution()
# for s in [inps[0]]:
for s in inps:
    print(f"Doing {s}...")
    ans = sol.minCut(s)
    print(" Got: ", ans)
