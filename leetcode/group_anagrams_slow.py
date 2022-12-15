"""Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        from collections import Counter

        anagram_dict = defaultdict(list)
        for s in strs:
            cnt = Counter(s)
            s_set = frozenset([(key, cnt[key]) for key in cnt])
            anagram_dict[s_set].append(s)
        return list(anagram_dict.values())


sol = Solution()
ans = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print("ANS: ", ans)
print("---------------------------------------")
inp = [
    "hos",
    "boo",
    "nay",
    "deb",
    "wow",
    "bop",
    "bob",
    "brr",
    "hey",
    "rye",
    "eve",
    "elf",
    "pup",
    "bum",
    "iva",
    "lyx",
    "yap",
    "ugh",
    "hem",
    "rod",
    "aha",
    "nam",
    "gap",
    "yea",
    "doc",
    "pen",
    "job",
    "dis",
    "max",
    "oho",
    "jed",
    "lye",
    "ram",
    "pup",
    "qua",
    "ugh",
    "mir",
    "nap",
    "deb",
    "hog",
    "let",
    "gym",
    "bye",
    "lon",
    "aft",
    "eel",
    "sol",
    "jab",
]
ans = sol.groupAnagrams(inp)
print("ANS: ", ans)
