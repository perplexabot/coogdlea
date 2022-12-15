"""There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?

Example 1:
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies
respectively.

Example 2:
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies
respectively. The third child gets 1 candy because it satisfies the above two conditions.
 """


class Solution:
    def candy(self, ratings: 'List[int]') -> int:
        if not ratings:
            return 0
        r = [(i, ind) for ind, i in enumerate(ratings)]
        r.sort(key=lambda x: x[0])
        C = {ind: 0 for ind in range(-1, len(ratings) + 1)}
        for val, ind in r:
            if ind - 1 > -1 and ratings[ind - 1] == val:
                if (ind + 1 < len(ratings) and ratings[ind + 1] == val) or (ind + 1 > len(ratings)):
                    C[ind] = 1
                else:
                    C[ind] = C[ind + 1] + 1
            elif ind + 1 < len(ratings) and ratings[ind + 1] == val:
                if ind - 1 < 0:
                    C[ind] = 1
                else:
                    C[ind] = C[ind - 1] + 1
            else:
                if ind - 1 > -1 and ind + 1 < len(ratings):
                    C[ind] = max(C[ind - 1], C[ind + 1]) + 1
                elif ind - 1 > -1:
                    C[ind] = C[ind - 1] + 1
                elif ind + 1 < len(ratings):
                    C[ind] = C[ind + 1] + 1
                else:
                    C[ind] = 1

        return sum(C.values())


inps = [
    ([1, 0, 2], 5),
    ([1, 2, 2], 4),
    ([5, 8, 4, 1, 6, 3, 1, 8, 4, 7], 18),
    ([1], 1),
    ([2, 2], 2),
    ([], 0),
    ([1, 2, 1, 2, 1, 2], 9),
    ([2] * 10, 10),
    ([1, 2, 3, 4, 5, 6], sum(range(7))),
    (None, 0),
]

sol = Solution()
for inp, exp in inps:
    print(f"Finding min candy for ranking {inp} and asserting...")
    ans = sol.candy(inp)
    assert ans == exp
