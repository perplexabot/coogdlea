def removeNthFromEnd(head, n):
    d = {}
    t = 1
    
    #save node in dic with a counter being used 
    # for keys 
    curr = head
    while curr:
        d[t] = curr
        curr = curr.next
        t += 1
    
    pos = len(d) - n + 1

    if pos == 1:
        head = head.next
    elif pos == len(d):
        d[pos-1].next = None
    else:
        d[pos].val = d[pos].next.val
        d[pos].next = d[pos].next.next
    return head
