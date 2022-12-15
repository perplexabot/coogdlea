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
        from operator import mul
        from functools import reduce

        primes = {
            'a': 2,
            'b': 3,
            'c': 5,
            'd': 7,
            'e': 11,
            'f': 13,
            'g': 17,
            'h': 19,
            'i': 23,
            'j': 29,
            'k': 31,
            'l': 37,
            'm': 41,
            'n': 43,
            'o': 47,
            'p': 53,
            'q': 59,
            'r': 61,
            's': 67,
            't': 71,
            'u': 73,
            'v': 79,
            'w': 83,
            'x': 89,
            'y': 97,
            'z': 101,
        }
        anagram_dict = defaultdict(list)
        for s in strs:
            val = reduce(mul, [primes[c] for c in s], 1)
            anagram_dict[val].append(s)
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
