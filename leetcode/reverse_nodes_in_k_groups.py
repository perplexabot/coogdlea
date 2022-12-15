# Given a linked list, reverse the nodes of a linked list k at
# a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length
# of the linked list. If the number of nodes is not a multiple of
# k then left-out nodes in the end should remain as it is.
#
# Example:
# Given this linked list: 1->2->3->4->5
#   For k = 2, you should return: 2->1->4->3->5
#   For k = 3, you should return: 3->2->1->4->5
#
# Note:
#   Only constant extra memory is allowed.
#   You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#   Oooo    Oooo    Oooo    Oooo    Oo

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        # returns head of new list (aka tail of old list)
        def reverseList(l):
            t1 = None
            curr = l
            while curr: 
                t0 = curr.next
                curr.next = t1
                t1 = curr
                curr = t0
            return t1

        # create list of sub linked list from original 
        # the last head may or may not need to be reversed
        kList = []
        curr = head
        while curr:
            kList.append(curr)
            for i in range(k):
                tmp = curr
                curr = curr.next
                if not curr:
                    break
            # if reached end, then assigne next to None
            if tmp:
                tmp.next = None

        # reverse the sub linked lists, except the last one
        # as it may not be of size k, in which case don't reverse
        # but append. 
            # reversing first len(kList)-1 lists
        newHeads = []
        for l in range( len(kList) - 1):
            newHeads.append( reverseList(kList[l]) )

            # checking if length of last list is k 
        curr = kList[-1]
        cnt = 0
        while curr:
            curr = curr.next
            cnt += 1

            # reverse or not last list depending on size
        lst = reverseList( kList[-1] ) if cnt == k else kList[-1]
        newHeads.append(lst)

        # append sublists together
        for i in range( len(newHeads) - 1 ):
            curr = newHeads[i]
            while curr:
                currTail = curr
                curr = curr.next
            currTail.next = newHeads[i+1]

        return newHeads[0]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

s = Solution()

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
ans = s.reverseKGroup(a, 2)
print('ans for k=2: ')
curr = ans
while curr:
    print( str( curr.val ) )
    curr = curr.next
print ( '------------------------------' )
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
ans = s.reverseKGroup(a, 3)
print('ans for k=3: ')
curr = ans
while curr:
    print( str( curr.val ) )
    curr = curr.next
print ( '------------------------------' )
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
ans = s.reverseKGroup(a, 5)
print('ans for k=5: ')
curr = ans
while curr:
    print( str( curr.val ) )
    curr = curr.next
print ( '------------------------------' )
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
ans = s.reverseKGroup(a, 1)
print('ans for k=1: ')
curr = ans
while curr:
    print( str( curr.val ) )
    curr = curr.next
print ( '------------------------------' )
a = ListNode(1)
ans = s.reverseKGroup(a, 1)
print('ans for k=1: ')
curr = ans
while curr:
    print( str( curr.val ) )
    curr = curr.next
print ( '------------------------------' )
a = ListNode(1)
a.next = ListNode(2)
ans = s.reverseKGroup(a, 1)
print('ans for k=1: ')
curr = ans
while curr:
    print( str( curr.val ) )
    curr = curr.next
print ( '------------------------------' )
a = ListNode(1)
a.next = ListNode(2)
ans = s.reverseKGroup(a, 2)
print('ans for k=2: ')
curr = ans
while curr:
    print( str( curr.val ) )
    curr = curr.next
