"""Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""


class Solution:
    def isInterleave(self, s1: 'str', s2: 'str', s3: 'str') -> 'bool':
        from collections import Counter

        if len(s1) + len(s2) != len(s3):
            return False

        if Counter(s1) + Counter(s2) != Counter(s3):
            return False

        visited = set()

        def helper(i1, i2, i3, qSet):
            if i3 == len(s3) and i2 == len(s2) and i1 == len(s1):
                qSet.add(True)

            if i1 < len(s1) and s1[i1] != s3[i3] and i2 < len(s2) and s2[i2] != s3[i3]:
                return

            if (
                i1 < len(s1)
                and s1[i1] == s3[i3]
                and True not in qSet
                and (i1 + 1, i2) not in visited
            ):
                visited.add((i1 + 1, i2))
                helper(i1 + 1, i2, i3 + 1, qSet)

            if (
                i2 < len(s2)
                and s2[i2] == s3[i3]
                and True not in qSet
                and (i1, i2 + 1) not in visited
            ):
                visited.add((i1, i2 + 1))
                helper(i1, i2 + 1, i3 + 1, qSet)

        quickSet = set([False])
        helper(0, 0, 0, quickSet)
        return True if True in quickSet else False


inps = [
    ('aabcc', 'dbbca', 'aadbbcbcac', True),
    ('aabcc', 'dbbca', 'aadbbbaccc', False),
    ('', '', '', True),
    ('', '', 'hey', False),
    ('hey', '', 'hey', True),
    ('', 'hey', 'hey', True),
    ('h', 'ey', 'hey', True),
    ('ph', 'ey', 'hey', False),
    ('h', 'eyp', 'hey', False),
    ('hp', 'ey', 'hey', False),
    ('hpi', 'ey', 'hey', False),
    ('hpi', 'ey', '', False),
    ('hpi', 'ey', '', False),
    ('aabbddef', 'aaefgg', 'aabbaaddeeffgg', True),
    (
        "cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc",
        "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb",
        "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb",
        True,
    ),
    (
        "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
        "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
        "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab",
        False,
    ),
]

sol = Solution()
for s1, s2, s3, exp in inps:
    print(f"Checking if s1[{s1}], s2[{s2}], s3[{s3}] are interleaved and asserting...")
    ans = sol.isInterleave(s1, s2, s3)
    assert ans == exp
    print('--------------------------------------')
