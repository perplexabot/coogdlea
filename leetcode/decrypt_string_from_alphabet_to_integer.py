"""
You are given a string s formed by digits and '#'. We want to map s to English lowercase
    characters as follows:
    - Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    - Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.
The test cases are generated so that a unique mapping will always exist.

Example 1:
    Input: s = "10#11#12"
    Output: "jkab"
    Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
    Input: s = "1326#"
    Output: "acz"

Constraints:
    1 <= s.length <= 1000
    s consists of digits and the '#' letter.
    s will be a valid string such that mapping is always possible.

A:
    digits (not numbers) so no negatives
    empty string return empty string
    malformed string -> not possible

D:
    replace things with # first
    replace things without # second
    return
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        from string import ascii_lowercase

        map_0 = {str(9 + num + 1) + '#': char for num, char in enumerate(ascii_lowercase[9:])}
        map_1 = {str(num + 1): char for num, char in enumerate(ascii_lowercase[:9])}

        for key in map_0:
            s = s.replace(key, map_0[key])

        for key in map_1:
            s = s.replace(key, map_1[key])

        return s


cases = [("10#11#12", "jkab"), ("1326#", "acz")]

sol = Solution()
for (s, exp) in cases:
    assert (
        got := sol.freqAlphabets(s)
    ) == exp, f"Failed case ({s}) - expecting ({exp}), got ({got})."
