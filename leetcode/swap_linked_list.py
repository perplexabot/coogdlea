"""Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""


class Node:
    def __init__(self, v, nxt=None):
        self.val = v
        self.next = nxt


def swapList(hd):
    if not hd:
        return hd

    if not hd.next:
        return hd

    head = hd.next

    def swap(pare, ndA):
        if ndA.next:
            ndB = ndA.next
            if pare:
                pare.next = ndB
            ndC = ndB.next
            ndB.next = ndA
            ndA.next = ndC

    curr = hd
    pare = None
    while curr:
        next_pare = curr
        next_curr = None if not curr.next else curr.next.next
        swap(pare, curr)
        curr = next_curr
        pare = next_pare

    return head


def linkedToList(hd):
    lst = []
    curr = hd
    while curr:
        lst.append(curr.val)
        curr = curr.next
    return lst


inps = [
    (Node(1, Node(2, Node(3, Node(4, None)))), [2, 1, 4, 3]),
    (Node(1), [1]),
    (Node(1, Node(2)), [2, 1]),
    (Node(1, Node(2, Node(3))), [2, 1, 3]),
    (Node(1, Node(2, Node(3, Node(4, Node(5))))), [2, 1, 4, 3, 5]),
    (None, []),
]

for hd, exp in inps:
    print(f"Swapping pairs for {linkedToList(hd)} and asserting...")
    newHd = swapList(hd)
    assert linkedToList(newHd) == exp
