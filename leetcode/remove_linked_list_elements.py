"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that
    has Node.val == val, and return the new head.

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

Example 2:
    Input: head = [], val = 1
    Output: []

Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

Constraints:
    The number of nodes in the list is in the range [0, 10**4].
    1 <= Node.val <= 50
    0 <= val <= 50

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

A:
    if head is None -> return None/head
    if head is 1 and to be removed -> return None
    if value to be removed is first -> new head 
    if value to be removed is last -> parent pointer becomes Null
    if value to be removed is middle -> parent pointer points to child
    if value not in list -> return list
    if value is consecutive in list?

D:
    if not head:
        return head

    # take care of single node case
    if not head.next:
        if head.val == target:
            return None
        else:
            return Head

    # take care of first node
    if head.val == target:
        head = head.next

    curr = head:
    while curr.next:
        if curr.next.val == target
            curr.next = curr.next.next
        curr = curr.next

    return head
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            if head.val == val:
                return None
            else:
                return head

        curr = head
        prev = None
        while curr:
            if curr.val == val:
                # fix parent
                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head


cases = [
    (
        ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))),
        6,
        [1, 2, 3, 4, 5],
    ),
    (None, 1, []),
    (ListNode(1), 1, []),
    (ListNode(1, ListNode(1)), 1, []),
    (ListNode(1, ListNode(2, ListNode(3))), 1, [2, 3]),
    (ListNode(3, ListNode(2, ListNode(1))), 1, [3, 2]),
    (ListNode(1, ListNode(1, ListNode(1))), 1, []),
    (ListNode(7, ListNode(7, ListNode(7, ListNode(7)))), 7, []),
]

sol = Solution()
for ind, (root, val, exp) in enumerate(cases):
    got = sol.removeElements(root, val)
    got_vals = []
    curr = got
    while curr:
        got_vals.append(curr.val)
        curr = curr.next
    assert got_vals == exp, f"Failed case ({ind}) - expecting ({exp}), got ({got_vals})"
