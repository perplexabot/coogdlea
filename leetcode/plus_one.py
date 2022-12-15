"""
You are given a large integer represented as an integer array digits, where each digits[i] is the
    ith digit of the integer. The digits are ordered from most significant to least significant in
    left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].

Example 2:
    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4,3,2,2].

Example 3:
    Input: digits = [9]
    Output: [1,0]
    Explanation: The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    Thus, the result should be [1,0].

Constraints:
    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain any leading 0's.

A:
    what if digits is empty             ->  return None
    what if digits contain non ints     ->  return None
    assume no leading zeros             ->  from constraint this is not possible
    what if digits represents negative  ->  from constraint this is not possible

D:
    join to string
    convert to int
    add one
    convert to string
    convert to list

    or

    start at least sig num, add 1
    place answer ones place in current spot
    carry the tens place and add to next least sig
    repeat until at end

P:
    carry = 1
    for ind,elem in enumerate(digits[::-1]):
        ind = len(digits) - ind - 1
        sum = i + carry
        ones = sum % 10
        carry //= 10
        digits[ind] = ones
    return [carry] + digits if carry else digits

"""


def plusOne(digits: list[int]) -> list[int]:
    if not digits:
        return None

    carry = 1
    final = digits[:]
    for ind, elem in enumerate(digits[::-1]):
        summation = elem + carry
        ones = summation % 10
        carry = summation // 10
        final[len(digits) - ind - 1] = ones
    return [carry] + final if carry else final


cases = [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1, 0]),
    ([], None),
    ([0], [1]),
    ([9, 9, 9], [1, 0, 0, 0]),
]

for (digits, exp) in cases:
    assert (
        ans := plusOne(digits)
    ) == exp, f"Failed with ({digits}) - expecting ({exp}), got ({ans})"
