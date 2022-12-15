"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

URL: https://leetcode.com/problems/fizz-buzz/
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        l = []
        for i in range(1, n + 1):
            if not i % 3 and not i % 5:
                l.append('FizzBuzz')
            elif not i % 3:
                l.append('Fizz')
            elif not i % 5:
                l.append('Buzz')
            else:
                l.append(str(i))
        return l


inps = [
    (1, ['1']),
    (0, []),
    (3, ['1', '2', 'Fizz']),
    (
        15,
        [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ],
    ),
]

sol = Solution()

for inp, exp in inps:
    assert (got := sol.fizzBuzz(inp)) == exp, f"failed {inp}, got {got}, expecting {exp}"
