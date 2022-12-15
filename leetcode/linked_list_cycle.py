"""Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position
(0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the
linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x, nxt):
        self.val = x
        self.next = nxt


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        s = set()
        curr = head
        while curr:
            if curr in s:
                return True
            s.add(curr)
            curr = curr.next
        return False


a = ListNode(1, None)
b = ListNode(2, None)
c = ListNode(3, None)
d = ListNode(4, None)
a.next = b
b.next = c
c.next = d
d.next = a
cyc0 = a

a = ListNode(1, None)
b = ListNode(2, None)
c = ListNode(3, None)
d = ListNode(4, None)
a.next = b
b.next = c
c.next = d
d.next = c
cyc1 = a

a = ListNode(1, None)
b = ListNode(2, None)
c = ListNode(3, None)
d = ListNode(4, None)
a.next = b
b.next = c
c.next = d
d.next = d
cyc2 = a

a = ListNode(1, None)
a.next = a
cyc3 = a

inps = [
    (ListNode(1, None), False),
    (ListNode(1, ListNode(2, ListNode(3, None))), False),
    (cyc0, True),
    (cyc1, True),
    (cyc2, True),
    (cyc3, True),
    (None, False),
]

sol = Solution()
for ind, (p, exp) in enumerate(inps):
    print(f"Checking if example[{ind}] contains cycle and asserting...")
    assert exp == sol.hasCycle(p)
