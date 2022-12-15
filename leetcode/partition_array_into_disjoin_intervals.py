"""
Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.

URL: https://leetcode.com/problems/partition-array-into-disjoint-intervals/

A:
    output can't equal 0 or len(A)
A:
    case with A = [x x ... x]
        1 1 1 1
         |
D:
    * is left max
    | is partition
    x is a hit, where hit is right[j] <= left[i]
    =======================
    5 0 3 8 6
    *|x
    5 0 3 8 6
    *  |x
    5 0 3 8 6
    *    |
    =======================
    1 1 1 0 6 12
    *|    x
    *      |

P:
    left_max = A[0]
    partition = 1
    # left = A[:partition]
    # right = A[parition:]
    for i in range(partition, len(A)):
        if left_max > A[i]:
            partition = i + 1
            left_max = max(A[:partition])
    return partition

O:
    could compare left_max with A[i] and save a potential max (vs max(A[:partition])). With this, the algo is O(n)


ADPOCT
"""


class Solution:
    def partitionDisjoint(self, A: 'List[int]') -> int:
        left_max = A[0]
        potential_left_max = left_max
        partition = 1

        for i in range(partition, len(A)):
            potential_left_max = max((potential_left_max, A[i]))
            if left_max > A[i]:
                partition = i + 1
                left_max = potential_left_max
        return partition


inps = [
    ([5, 0, 3, 8, 6], 3),
    ([1, 1, 1, 0, 6, 12], 4),
    ([1, 2], 1),
    ([1, 1, 1, 1], 1),
    ([1, 0, 1, 0, 1], 4),
    ([1, 1], 1),
    ([32, 57, 24, 19, 0, 24, 49, 67, 87, 87], 7),
]

sol = Solution()
for inp, exp in inps:
    assert exp == (
        ans := sol.partitionDisjoint(inp)
    ), f"inp: {inp}, exp: {exp}, got: {ans}, left = {inp[:ans]}, right = {inp[ans:]}"
