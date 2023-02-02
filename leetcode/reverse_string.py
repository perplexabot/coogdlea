"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

Constraints:
    1 <= s.length <= 10**5
    s[i] is a printable ascii character.

A:
    given an empty list -> return empty
    given list if 1     ->  return list
    given list of 2     ->  switch and return

D:
    Input: s = ["h","e","l","l","o"]
    len(s) = 5
    mid = 5 // 2 = 2
    curr = 0:
        s[curr],s[-1-curr] = s[curr],s[-1-curr]
    curr = 1:
        s[curr],s[-1-curr] = s[curr],s[-1-curr]

    Input: s = ["H","a","n","n","a","h"]
    len(s) = 6
    mid = 6 //2 = 3
    curr = 0:
        s[curr],s[-1-curr] = s[curr],s[-1-curr]
    curr = 1:
        s[curr],s[-1-curr] = s[curr],s[-1-curr]
    curr = 2:
        s[curr],s[-1-curr] = s[curr],s[-1-curr]
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]


sol = Solution()

cases = [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    (["a"], ["a"]),
    (["a", "b"], ["b", "a"]),
]

for (s, exp) in cases:
    sol.reverseString(s)
    assert s == exp, f"Failed. Expecting {exp}, got {s}"
