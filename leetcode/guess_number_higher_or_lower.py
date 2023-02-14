"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or
    lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

    - -1: Your guess is higher than the number I picked (i.e. num > pick).
    - 1: Your guess is lower than the number I picked (i.e. num < pick).
    - 0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:
    Input: n = 10, pick = 6
    Output: 6

Example 2:
    Input: n = 1, pick = 1
    Output: 1

Example 3:
    Input: n = 2, pick = 1
    Output: 1

Constraints:
    1 <= n <= 2**31 - 1
    1 <= pick <= n

A:
    n = 4, pick = 2
    g = n // 2 = 2
    guess(g) = 0; return 2

    n = 4 pick = 1
    g = n //2 = 2
    guess(g) = 1

"""


def guess(g):
    global pick
    if g < pick:
        return 1
    if g > pick:
        return -1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        from math import ceil

        left = 0
        right = n
        g = left + ceil((right - left) / 2)
        while True:
            print(f"g: {g}")
            if not guess(g):
                return g
            elif guess(g) == -1:
                right = g
            else:
                left = g
            g = left + ceil((right - left) / 2)


sol = Solution()
cases = [(10, 6), (1, 1), (2, 1)]
for (n, pick) in cases:
    assert (
        got := sol.guessNumber(n)
    ) == pick, f"Failed case ({n}, {pick}) - expecting ({pick}), got ({got})"
