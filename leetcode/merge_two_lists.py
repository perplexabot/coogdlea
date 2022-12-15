# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    curr = None
    hd = curr
    while l1 and l2:
        if l1.val <= l2.val:
            if not hd:
                hd = l1
                curr = hd
            else:
                curr.next = l1
                curr = curr.next
            l1 = l1.next
        else:
            if not hd:
                hd = l2
                curr = hd
            else:
                curr.next = l2
                curr = curr.next
            l2 = l2.next

    if l1:
        if not hd:
            hd = l1
        else:
            curr.next = l1
    
    if l2:
        if not hd:
            hd = l2
        else:
            curr.next = l2

    return hd


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

c = mergeTwoLists(a,b)

curr = c
while curr:
    print( str(curr.val) )
    curr = curr.next

a = None

b = ListNode(1)

c = mergeTwoLists(a,b)

curr = c
while curr:
    print( str(curr.val) )
    curr = curr.next
