"""
You are given an integer array ranks and a character array suits. You have 5 cards where
    the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:
    "Flush": Five cards of the same suit.
    "Three of a Kind": Three cards of the same rank.
    "Pair": Two cards of the same rank.
    "High Card": Any single card.

Return a string representing the best type of poker hand you can make with the given cards.
Note that the return values are case-sensitive.

Example 1:
    Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
    Output: "Flush"
    Explanation: The hand with all the cards consists of 5 cards with the same suit, so we have a "Flush".

Example 2:
    Input: ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
    Output: "Three of a Kind"
    Explanation: The hand with the first, second, and fourth card consists of 3 cards with the
        same rank, so we have a "Three of a Kind".
    Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
    Also note that other cards could be used to make the "Three of a Kind" hand.

Example 3:
    Input: ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
    Output: "Pair"
    Explanation: The hand with the first and second card consists of 2 cards with the same rank, so we have a "Pair".
    Note that we cannot make a "Flush" or a "Three of a Kind".

Constraints:
    ranks.length == suits.length == 5
    1 <= ranks[i] <= 13
    'a' <= suits[i] <= 'd'
    No two cards have the same rank and suit.

A:
    one poker hand will always be satisfied
    len of ranks and suits should always be 5

D:
    ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
    if len(set(suits)) == 5: return "Flush"

    ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
    if len(set(suits)) == 5: return "Flush"
    if len(set(ranks)) >= 3: return "Three of"

    ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
    if len(set(suits)) == 5: return "Flush"
    if len(set(ranks)) >= 3: return "Three of"
    if len(set(ranks)) == 2: return "Pair"
"""


def bestHand(ranks: list[int], suits: list[str]) -> str:
    from collections import Counter

    cnts = Counter(ranks)
    if len(set(suits)) == 1:
        return "Flush"
    if any(x > 2 for x in set(cnts.values())):
        return "Three of a Kind"
    if 2 in set(cnts.values()):
        return "Pair"
    return "High Card"


cases = [
    ([13, 2, 3, 1, 9], ["a", "a", "a", "a", "a"], "Flush"),
    ([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"], "Three of a Kind"),
    ([10, 10, 2, 12, 9], ["a", "b", "c", "a", "d"], "Pair"),
    ([1, 2, 3, 4, 5], ["a", "b", "c", "a", "d"], "High Card"),
    ([2, 10, 7, 10, 7], ["a", "b", "a", "d", "b"], "Pair"),
]

for (ranks, suits, exp) in cases:
    assert (
        got := bestHand(ranks, suits)
    ) == exp, f"Failed case ({ranks}, {suits}) - got ({got}), expecting ({exp})"
