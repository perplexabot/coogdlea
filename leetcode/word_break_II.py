"""Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word. Return
all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


class Solution:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> 'List[str]':
        from collections import defaultdict

        if not wordDict:
            return []

        wD = set(wordDict)
        childs = defaultdict(list)
        childs[len(s)] = [None]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wD and j in childs:
                    childs[i].append(j)

        paths = []

        def dfs(nd, path):
            if nd is None:
                paths.append(path)
                return

            for ch in childs[nd]:
                dfs(ch, ' '.join([path, s[nd:ch]]))

        dfs(0, '')
        return [x.strip() for x in paths]


import pprint

inps = [
    ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
    ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
    ("a", ['a']),
    ("abc", ['abc', 'a', 'b', 'c']),
    ("hellow", []),
    (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        [
            "a",
            "aa",
            "aaa",
            "aaaa",
            "aaaaa",
            "aaaaaa",
            "aaaaaaa",
            "aaaaaaaa",
            "aaaaaaaaa",
            "aaaaaaaaaa",
        ],
    ),
    (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        [
            "a",
            "aa",
            "aaa",
            "aaaa",
            "aaaaa",
            "aaaaaa",
            "aaaaaaa",
            "aaaaaaaa",
            "aaaaaaaaa",
            "aaaaaaaaaa",
        ],
    ),
]

sol = Solution()
for s, wd in inps:
    print(f"Doing s[{s}] and wd[{wd}]...")
    ans = sol.wordBreak(s, wd)
    pprint.pprint(ans)
