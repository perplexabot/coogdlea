"""Given two words word1 and word2, find the minimum number of operations required to convert
word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)

        if not word2:
            return len(word1)

        d = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            d[i][0] = i

        for i in range(1, len(word2) + 1):
            d[0][i] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                weight = 1 if word1[i - 1] != word2[j - 1] else 0
                d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + weight)

        return d[-1][-1]


inps = [
    ('horse', 'ros', 3),
    ('intention', 'execution', 5),
    ('1abcdef1', 'abcdef', 2),
    ('a', 'b', 1),
]

sol = Solution()
for w1, w2, exp in inps:
    print(f"Finding min distance between {w1} and {w2} and asserting...")
    ans = sol.minDistance(w1, w2)
    print(f" Got: {ans}")
    # assert ans == exp
