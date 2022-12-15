"""Given an array of numbers and an index i, return the index of the nearest larger number of the
number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i
doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""


class Solution:
    def __init__(self, arr):
        self.arr = arr
        self.d = {ind: self.nearestLarger(ind) for ind in range(len(self.arr))}

    def getNearestLarger(self, ind):
        return self.d[ind]

    def nearestLarger(self, ind):
        if ind < 0 or ind > len(self.arr):
            raise KeyError

        if self.arr[ind] == max(self.arr):
            return None

        j, leftLarger = ind - 1, None
        while j > -1:
            if self.arr[j] > self.arr[ind]:
                leftLarger = j
                break
            j -= 1

        j, rightLarger = ind + 1, None
        while j < len(self.arr):
            if self.arr[j] > self.arr[ind]:
                rightLarger = j
                break
            j += 1

        return leftLarger if not rightLarger else rightLarger


inps = [
    ([4, 1, 2, 5, 6], 0, 3),
    ([1, 1, 1, 1, 1, 1], 1, None),
    ([1, 2, 3], 2, None),
    ([5, 4, 3, 2, 1, 2, 3, 4, 5], 4, 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 4),
    ([1], 0, None),
    ([1, 2, 1], 1, None),
    ([1, 2, 3, 4], 0, 1),
    ([4, 3, 2, 1], 0, None),
    ([1, 2, 3, 4], 3, None),
    ([4, 3, 2, 1], 3, 2),
    ([5, 1, 2, 3, 4, 3, 2, 1], 4, 0),
    ([1, 2, 3, 4, 3, 2, 1, 5], 3, 7),
]

for arr, ind, exp in inps:
    print(f"Finding nearest larger for index[{ind}] in {arr} and asserting...")
    sol = Solution(arr)
    ans = sol.getNearestLarger(ind)
    assert ans == exp
