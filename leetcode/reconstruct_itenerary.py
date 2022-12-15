"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus,
the itinerary must begin with JFK.

Note:
    * If there are multiple valid itineraries, you should return the itinerary that has the smallest
        lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a
        smaller lexical order than ["JFK", "LGB"].
    * All airports are represented by three capital letters (IATA code).
    * You may assume all tickets form at least one valid itinerary.
    * One must use all the tickets once and only once.

Example 1:
    Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
    Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
                 But it is larger in lexical order.

URL: https://leetcode.com/problems/reconstruct-itinerary/
START: 4:42

ADAPOCT
"""


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        from collections import defaultdict
        from collections import deque

        d = defaultdict(list)

        for t in tickets:
            d[t[0]].append(t[1])

        for k in d:
            d[k] = deque(sorted(d[k]))

        at = 'JFK'
        it = [at]

        while d[at]:
            at = d[at].popleft()
            it.append(at)

        return it if tickets else []


inps = [
    (
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
        ["JFK", "MUC", "LHR", "SFO", "SJC"],
    ),
    (
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
        ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
    ),
    ([], []),
    ([['JFK', 'ATL']], ['JFK', 'ATL']),
    ([['JFK', 'ATL'], ['ATL', 'JFK']], ['JFK', 'ATL', 'JFK']),
]

sol = Solution()
for inp, exp in inps:
    assert (ans := sol.findItinerary(inp)) == exp, f"failed {inp}. Got {ans}, expected {exp}"
