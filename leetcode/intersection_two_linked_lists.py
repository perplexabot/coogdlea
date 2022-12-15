"""Write a program to find the node at which the intersection of two singly linked lists begins.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0
if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the
head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node
in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if
the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head
of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There
are 1 node before the intersected node in B.


Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads
as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and
skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        currA = headA
        currB = headB

        cntA = 0
        while currA:
            cntA += 1
            currA = currA.next

        cntB = 0
        while currB:
            cntB += 1
            currB = currB.next

        currA = headA
        currB = headB
        if cntA > cntB:
            for i in range(cntA - cntB):
                currA = currA.next
        if cntB > cntA:
            for i in range(cntB - cntA):
                currB = currB.next

        try:
            while currA != currB:
                currA = currA.next
                currB = currB.next
        except AttributeError:
            return None

        return currA


inter_nd0 = ListNode(2, ListNode(4, None))
inter_nd1 = ListNode(8, ListNode(4, ListNode(5, None)))
inter_nd5 = ListNode(777, None)
inter_nd6 = ListNode(777, None)
inter_nd7 = ListNode(777, None)

inps = [
    (ListNode(0, ListNode(9, ListNode(1, inter_nd0))), ListNode(3, inter_nd0), inter_nd0),
    (
        ListNode(4, ListNode(1, inter_nd1)),
        ListNode(5, ListNode(0, ListNode(1, inter_nd1))),
        inter_nd1,
    ),
    (ListNode(2, ListNode(6, ListNode(4, None))), ListNode(1, ListNode(5, None)), None),
    (ListNode(2, ListNode(6, ListNode(4, None))), None, None),
    (None, ListNode(1, ListNode(5, None)), None),
    (ListNode(0, ListNode(1, inter_nd5)), ListNode(2, ListNode(3, inter_nd5)), inter_nd5),
    (inter_nd6, inter_nd6, inter_nd6),
    (ListNode(0, ListNode(1, ListNode(2, inter_nd7))), inter_nd7, inter_nd7),
]

sol = Solution()
for ind, (lstA, lstB, exp) in enumerate(inps):
    print(f"Doing example[{ind}] and asserting...")
    assert exp is sol.getIntersectionNode(lstA, lstB)
