class node:
    def __init__(self, v):
        self.v = v
        self.next = None

def swapPairs(head):
    def reverseAndConnectPair(pairHead, externalConnection):
        if not pairHead:
            externalConnection.next = None
        else:
            if pairHead.next:
                if externalConnection:
                    externalConnection.next = pairHead.next

                nxtNd = pairHead.next.next
                pairHead.next.next = pairHead
                reverseAndConnectPair(nxtNd, pairHead)
            else:
                externalConnection.next = pairHead

    if not head:
        return None
    if not head.next:
        return head
    
    newHead = head.next
    reverseAndConnectPair(head, None)
    return newHead

def printList(h):
    curr = h
    while curr:
        print(str(curr.v))
        curr = curr.next

head = node(0)
curr = head
for i in range(1,1):
    curr.next = node(i)
    curr = curr.next

print("init list: ")
printList(head)

ans = swapPairs(head)
print("ans: ")
printList(ans)
