# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 
# Example:
# 
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq 
        ts = [ (lists[i].val, hash(lists[i]), lists[i]) for i in range( len(lists) ) if lists[i] ]
        heapq.heapify(ts)

        hd = None if not ts else heapq.heappop(ts)[2]
        curr = hd
        if hd and hd.next:
            heapq.heappush( ts, (hd.next.val, hash(hd.next),  hd.next) )

        while ts:
            val, hs, nd = heapq.heappop(ts)
            if nd.next:
                heapq.heappush( ts, (nd.next.val, hash(nd.next),  nd.next) )
            curr.next = nd
            curr = nd
        return hd

l0 = ListNode(1)
l0.next = ListNode(4)
l0.next.next = ListNode(5)

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)

l2 = ListNode(2)
l2.next = ListNode(6)

for ind, i in enumerate( [l0, l1, l2] ):
    curr = i
    print( ''.join( [ 'l', str(ind), ': ' ] ) )
    while curr:
        print( str( curr.val) )
        curr = curr.next

aSol = Solution()
ans = aSol.mergeKLists( [l0, l1, l2] )
print( 'Merged: ' )
curr = ans 
while curr:
    print( str( curr.val ) )
    curr = curr.next

print('----------------------------------------')

l0 = ListNode(1)

l1 = ListNode(1)

l2 = ListNode(2)

for ind, i in enumerate( [l0, l1, l2] ):
    curr = i
    print( ''.join( [ 'l', str(ind), ': ' ] ) )
    while curr:
        print( str( curr.val) )
        curr = curr.next

aSol = Solution()
ans = aSol.mergeKLists( [l0, l1, l2] )
print( 'Merged: ' )
curr = ans 
while curr:
    print( str( curr.val ) )
    curr = curr.next

print('----------------------------------------')
for ind, i in enumerate( [] ):
    curr = i
    print( ''.join( [ 'l', str(ind), ': ' ] ) )
    while curr:
        print( str( curr.val) )
        curr = curr.next

aSol = Solution()
ans = aSol.mergeKLists( [] )
print( 'Merged: ' )
curr = ans 
while curr:
    print( str( curr.val ) )
    curr = curr.next

print('----------------------------------------')
for ind, i in enumerate( [None, None] ):
    curr = i
    print( ''.join( [ 'l', str(ind), ': ' ] ) )
    while curr:
        print( str( curr.val) )
        curr = curr.next

aSol = Solution()
ans = aSol.mergeKLists( [None, None] )
print( 'Merged: ' )
curr = ans 
while curr:
    print( str( curr.val ) )
    curr = curr.next

print('----------------------------------------')
for ind, i in enumerate( [[]] ):
    curr = i
    print( ''.join( [ 'l', str(ind), ': ' ] ) )
    while curr:
        print( str( curr.val) )
        curr = curr.next

aSol = Solution()
ans = aSol.mergeKLists( [[]] )
print( 'Merged: ' )
curr = ans 
while curr:
    print( str( curr.val ) )
    curr = curr.next

print('----------------------------------------')
for ind, i in enumerate( [[],[]] ):
    curr = i
    print( ''.join( [ 'l', str(ind), ': ' ] ) )
    while curr:
        print( str( curr.val) )
        curr = curr.next

aSol = Solution()
ans = aSol.mergeKLists( [[],[]] )
print( 'Merged: ' )
curr = ans 
while curr:
    print( str( curr.val ) )
    curr = curr.next

print('----------------------------------------')
l1 = ListNode(1)
for ind, i in enumerate( [l1] ):
    curr = i
    print( ''.join( [ 'l', str(ind), ': ' ] ) )
    while curr:
        print( str( curr.val) )
        curr = curr.next

aSol = Solution()
ans = aSol.mergeKLists( [l1] )
print( 'Merged: ' )
curr = ans 
while curr:
    print( str( curr.val ) )
    curr = curr.next
