"""
You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either
    fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2]
    denote the number of cold, warm, and hot water cups you need to fill respectively. Return the
    minimum number of seconds needed to fill up all the cups.

Example 1:
    Input: amount = [1,4,2]
    Output: 4
    Explanation: One way to fill up the cups is:
    Second 1: Fill up a cold cup and a warm cup.
    Second 2: Fill up a warm cup and a hot cup.
    Second 3: Fill up a warm cup and a hot cup.
    Second 4: Fill up a warm cup.
    It can be proven that 4 is the minimum number of seconds needed.

Example 2:
    Input: amount = [5,4,4]
    Output: 7
    Explanation: One way to fill up the cups is:
    Second 1: Fill up a cold cup, and a hot cup.
    Second 2: Fill up a cold cup, and a warm cup.
    Second 3: Fill up a cold cup, and a warm cup.
    Second 4: Fill up a warm cup, and a hot cup.
    Second 5: Fill up a cold cup, and a hot cup.
    Second 6: Fill up a cold cup, and a warm cup.
    Second 7: Fill up a hot cup.

Example 3:
    Input: amount = [5,0,0]
    Output: 5
    Explanation: Every second, we fill up a cold cup.

Constraints:
    amount.length == 3
    0 <= amount[i] <= 100

A:
    amount always of size 3
    amount only contains ints
    if one amount is 0, use doubles until one is full, then use singles
    if two amount is 0, use singles until on is full
    if three are 0, return 0
    if none are zero, pick max and min and use doubles,
        then pick the two left overs and use doubles,
        if you have one more, use singles
        (trying to maximize the double usage, so grab the smallest one with the biggest one)

D:
                     C W H
    Input: amount = [1,4,2]
    min and max = C & W -> [0, 3, 2]    1
    do left over = W & H -> [0, 2, 1]   2
    do left over = W & H -> [0, 1, 0]   3
    do left over = W & H -> [0, 0, 0]   4

                     C W H
    Input: amount = [5,4,4]
    min and max = C & W -> [4,3,4] 1
    min and max = C & W -> [3,2,4] 2
    min and max = C & H -> [2,2,3] 3
    min and max = C & H -> [1,2,2] 4
    min and max = C & H -> [0,2,1] 5
    min and max = W & H -> [0,1,0] 6
    do left over= W -> [0,0,0] 7

P:
    fills = 0
    while x != [0,0,0]:
        maxind = getMax
        minind = getMin
        x[maxind] -= 1
        x[minind] -= 1
        fills += 1
"""


def getMinIndex(x):
    y = [e if e else float('inf') for e in x]
    mi = 0
    if y[1] < y[mi]:
        mi = 1
    if y[2] < y[mi]:
        mi = 2
    return mi


def getMaxIndex(x):
    mi = 0
    if x[1] > x[mi]:
        mi = 1
    if x[2] > x[mi]:
        mi = 2
    return mi


def fillCups(amount: list[int]) -> int:
    fills = 0

    while amount != [0, 0, 0]:
        done = amount.count(0)
        if done == 0:
            amount[getMinIndex(amount)] -= 1
            amount[getMaxIndex(amount)] -= 1
            fills += 1
        elif done == 1:
            inds = [ind for ind, elem in enumerate(amount) if elem]
            amount[inds[0]] -= 1
            amount[inds[1]] -= 1
            fills += 1
        else:
            fills += sum(amount)
            amount = [0, 0, 0]
    return fills


cases = [
    ([1, 4, 2], 4),
    ([5, 4, 4], 7),
    ([5, 0, 0], 5),
    ([0, 0, 0], 0),
    ([1, 1, 1], 2),
    ([0, 0, 1], 1),
    ([0, 1, 0], 1),
    ([1, 0, 0], 1),
    ([1, 0, 1], 1),
    ([0, 1, 1], 1),
]

for (amounts, exp) in cases:
    assert (
        got := fillCups(amounts)
    ) == exp, f"Failed case ({amounts}) - expecting ({exp}), got ({got})"
