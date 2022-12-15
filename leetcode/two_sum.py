"""Given a list of numbers and a number k, return whether any 
two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

import pytest
def two_sum(a_list, target):
    """FInd if any two elements in a_list sum to target"""
    needed = set()
    l_set = set(a_list)

    for i in l_set:
        if i in needed:
            return True
        else:
            needed.add(target-i)
    return False

@pytest.mark.parametrize('lst, target, expected',
                         [
                             ([10, 3, 4, 6, 8], 14, True),
                             ([1, 2, 3, 4, 5], 100, False),
                             ([1], 1, False),
                             ([1, 1, 1, 1], 1, False),
                             ([1, 1, 1, 1], 3, False),
                             ([0, 3, 1, 1], 3, True),
                             ([3, -3, 1, 1], 0, True),
                             ([-3, 3, 1, 1], 0, True),
                             ([], 1, False),
                         ]
                        )
def test_func(lst, target, expected):
    """pytest function"""
    assert two_sum(lst, target) == expected
