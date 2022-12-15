"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant
space. In other words, find the lowest positive integer that does not exist in the array. The array
can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

import pytest

def find_lowest_not_there(a_list):
    """function to find smallest positive not in list
    Args:
        a_list:     a list of numbers
    Returns:
        curr_min:   the minimum positve number not in a_list
    """
    curr_min = float('inf')
    for number in a_list:
        # optimize this by preparse original list and replace none positives with +inf
        if number < 1:
            continue

        if curr_min == number:
            curr_min += 1
        else:
            curr_min = min(curr_min, number)
            if curr_min == number:
                while curr_min in a_list:
                    curr_min += 1
    return 1 if curr_min < 1 or curr_min == float('inf') else curr_min

@pytest.mark.parametrize('data_in, expected_out', [([3, 4, -1, 1], 2),
                                                   ([1, 2, 0], 3),
                                                   ([], 1),
                                                   ([-1], 1),
                                                   ([1], 2),
                                                   ([-50,-4], 1),
                                                   ([0,0,2,1,3,4], 5),
                                                  ])
def test_func(data_in, expected_out):
    """function to test find_lowest_not_there function
    Args:
        data_in: the list of numbers to be passed to find_lowest_not_there()
        expected_out:   the expected output of find_lowest_not_there() given data_in
    """
    assert expected_out == find_lowest_not_there(data_in)
