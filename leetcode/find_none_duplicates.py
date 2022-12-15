"""Given an array of integers in which two elements appear exactly
once and all other elements appear exactly twice, find the two
elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4
and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""


def extract_uniques(lst):
    from functools import reduce

    xor = reduce(lambda x, y: x ^ y, lst)

    mask = 1
    while not mask and xor:
        mask << 1

    x, y = 0, 0
    for n in lst:
        if mask & n:
            x ^= n
        else:
            y ^= n

    return x, y


inps = [([1, 2, 1, 2, 3, 4, 5, 6, 5, 6], (3, 4)), ([1, 1, 2, 2, 3, 3, 4, 5, 6, 6], (4, 5))]

from collections import Counter

for lst, exp in inps:
    print("Finding uniques in {lst} and asserting")
    ans = extract_uniques(lst)
    assert Counter(ans) == Counter(exp)
