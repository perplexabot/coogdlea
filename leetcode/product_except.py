"""Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
would be [2, 3, 6].

Follow-up: what if you can't use division?

"""
from functools import reduce
from operator import mul

def product_except(a_list):
    """read comment above"""
    # check a_list is valid
    # check if list is only one num
    if not a_list.count(0):
        a_list_red = reduce(mul, a_list)
        return [a_list_red/positive_num for positive_num in a_list]

    ans = [0]*len(a_list)

    if a_list.count(0) > 1:
        return ans

    zero_ind = a_list.index(0)
    ans[zero_ind] = reduce(mul, a_list.remove(0))
    return ans

def my_division(a,b):
    if b == 0:
        return None
    if a == 0:
        return 0
    # do stuff here
    return sign * ans
