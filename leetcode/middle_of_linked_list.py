"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100

Definition for singly-linked list:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
A:
    Empty list          ->  return None
    list of size 1      ->  return root/head
    list of size 2      ->  return tail
    list of size > 2    ->  find middle
    linked list is not circular

D:
    Input: head = [1,2,3,4,5]
    l = [node for node in head]
    return l[len(l)//2]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        l = []
        curr = head
        while curr:
            l.append(curr)
            curr = curr.next

        return l[len(l) // 2]


cases = [
    (ListNode(1, ListNode(2, (exp := ListNode(3, ListNode(4, ListNode(5)))))), exp),
    (ListNode(1, ListNode(2, ListNode(3, (exp := ListNode(4, ListNode(5, ListNode(6))))))), exp),
    ((exp := ListNode(1)), exp),
    (ListNode(0, (exp := ListNode(1))), exp),
]

sol = Solution()
for (index, case) in enumerate(cases):
    head, exp = case
    assert (
        got := sol.middleNode(head)
    ) == exp, f"Failed case {index} - got val {got.val}, expecting {exp.val}"
