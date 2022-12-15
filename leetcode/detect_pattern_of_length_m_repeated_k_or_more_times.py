"""
Given an array of positive integers arr, find a pattern of length m that is repeated
    k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values,
    repeated multiple times consecutively without overlapping. A pattern is defined by
    its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times,
    otherwise return false.

Example 1:
    Input: arr = [1,2,4,4,4,4], m = 1, k = 3
    Output: true
    Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern
        can be repeated k or more times but not less.

Example 2:
    Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
    Output: true
    Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. Another valid
        pattern (2,1) is also repeated 2 times.

Example 3:
    Input: arr = [1,2,1,2,1,3], m = 2, k = 3
    Output: false
    Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern
        of length 2 that is repeated 3 or more times.

Constraints:
    2 <= arr.length <= 100
    1 <= arr[i] <= 100
    1 <= m <= 100
    2 <= k <= 100

A:
    array is empty and m = 0    -> return true
    array is empty and m != 0   -> return false
    k * m > length(array)       -> return false
    m > length(array)           -> return false

D:
    if length(arr) < m:
        return False

    if m == 1 and arr:
        return True

    start = m
    end = m + m
    count = 1
    curr_pattern = arr[0:m]
    while end < length(arr):
        while curr_pattern == arr[start:end]:
            count += 1
            start = end
            end = start + m
        
        if count >= k:
            return True

        start = end
        end = start + m
        curr_pattern = arr[start:end]
        count = 1
        
"""


def containsPattern(arr: list[int], m: int, k: int) -> bool:
    if not arr and not m:
        return True
    if len(arr) < m:
        return False
    if m == 1 and k == 1 and arr:
        return True
    if m * k > len(arr):
        return False

    index = 0

    while index + m < len(arr) + 1:
        start = index
        end = start + m

        count = 0
        curr_pattern = arr[start:end]
        while curr_pattern == arr[start:end]:
            count += 1
            start = end
            end = start + m

        if count >= k:
            return True

        index += 1
    return False


# This version assumes that the patterns can occur with elements in between, e.g: 12xxx12y12
# however the question does not ask for that
# def containsPattern(arr: list[int], m: int, k: int) -> bool:
#    s = 0
#    e = s + m
#    subarrs = []
#    while e < len(arr) + 1:
#        subarrs.append(''.join([str(x) for x in arr[s:e]]))
#        s += 1
#        e = s + m
#
#    sarry = str(''.join([str(x) for x in arr]))
#    for sub in subarrs:
#        print(f"sub: {sub}, sarry: {sarry}")
#        if sarry.count(sub) >= k:
#            return True
#    return False


cases = [
    ([1, 2, 4, 4, 4, 4], 1, 3, True),
    ([1, 2, 1, 2, 1, 1, 1, 3], 2, 2, True),
    ([1, 2, 1, 2, 1, 3], 2, 3, False),
    ([], 1, 1, False),
    ([1], 1, 1, True),
    ([1, 1], 1, 1, True),
    ([1, 1], 4, 1, False),
    ([], 0, 0, True),
    ([1, 2, 3, 1, 2], 2, 2, False),
    ([1, 2], 1, 2, False),
    ([1, 1], 1, 2, True),
    ([3, 6, 6, 6, 5, 1, 5, 2, 2, 3, 1, 5, 2, 6, 1, 5, 1, 2, 6, 3, 3, 5, 3, 6, 3, 4], 6, 2, False),
    ([3, 2, 2, 1, 2, 2, 1, 1, 1, 2, 3, 2, 2], 3, 2, True),
]

for (arr, m, k, exp) in cases:
    assert (
        ans := containsPattern(arr, m, k)
    ) == exp, f"Failed ({arr}, {m}, {k}) - expecting ({exp}), got ({ans})"
