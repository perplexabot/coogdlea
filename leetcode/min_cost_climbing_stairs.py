"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: You will start at index 1.
    - Pay 15 and climb two steps to reach the top.
    The total cost is 15.

Example 2:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: You will start at index 0.
    - Pay 1 and climb two steps to reach index 2.
    - Pay 1 and climb two steps to reach index 4.
    - Pay 1 and climb two steps to reach index 6.
    - Pay 1 and climb one step to reach index 7.
    - Pay 1 and climb two steps to reach index 9.
    - Pay 1 and climb one step to reach the top.
    The total cost is 6.

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999

A:
    cost of length 0 -> return 0
    cost of length 1 -> return cost[0]
    cost contains none int -> error out
    cost contains int < 0
A:
    ?
D:
    [10,15,20]
    start at 0:
        10 -> 15 -> 20 -> end (45)
        10 -> 15 -> end (25)
        10 -> 20 -> end (30)
    start at 1:
        15 -> 20 -> end (35)
        15 -> end (15)
P:
    if len(cost) == 0:
        return 0
    if len(cost) == 1:
        return cost[0]

    costs_from_0 = bfs(cost, start=0)
    costs_from_1 = bfs(cost, start=1)
    return min(costs_from_0 + costs_from_1)
"""


def minCostClimbingStairs(cost: list[int]) -> int:
    if len(cost) == 0:
        return 0
    if len(cost) == 1:
        return cost[0]

    from collections import deque

    def bfs(lst):
        Q = deque([(0, 0)])
        smallest = float('inf')
        while Q:
            curr_ind, curr_cost = Q.popleft()
            if curr_ind + 2 < len(lst):
                Q.append((curr_ind + 2, curr_cost + lst[curr_ind]))
                Q.append((curr_ind + 1, curr_cost + lst[curr_ind]))
            elif curr_ind + 1 < len(lst):
                smallest = min(smallest, curr_cost + lst[curr_ind])
                Q.append((curr_ind + 1, curr_cost + lst[curr_ind]))
            else:
                smallest = min(smallest, curr_cost + lst[curr_ind])
        return smallest

    return min(bfs(cost), bfs(cost[1:]))


def minCostClimbingStairs_better(cost: list[int]) -> int:
    """mincost(i) = cost[i] + min(mincost(i-1), mincost(i-2))"""

    modcost = cost + [0]

    save = {}

    def mincost(i):
        if i < 2:
            return modcost[i]

        if i in save:
            return save[i]

        save[i] = modcost[i] + min(mincost(i - 2), mincost(i - 1))
        return save[i]

    return mincost(len(cost))


cases = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    #    ([], 0),
    #    ([1], 1),
    #    ([0], 0),
    ([0, 0, 0, 0], 0),
    ([0, 1, 2], 1),
]

for (cost, exp) in cases:
    assert (
        ans := minCostClimbingStairs_better(cost)
    ) == exp, f"Failed ({cost}) - got ({ans}), expecting ({exp})"
