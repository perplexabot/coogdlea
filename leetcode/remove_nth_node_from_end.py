def removeNthFromEnd(head, n):
    def removeNth (head, startNd, n, sz):
        if n == 1:
            if head is startNd:
                startNd = startNd.next
                head = startNd
            else:
                startNd = startNd.next
                
        elif n == sz:
            curr = startNd
            t = 1
            while t < sz-1:
                curr = curr.next
                t += 1
            curr.next = None
        else:
            t = 1
            curr = startNd
            while t < n:
                curr = curr.next
                t += 1
            curr.val = curr.next.val
            curr.next = curr.next.next
        return head

    currFast = head
    mid = head
    ln = 1
    while currFast.next:
        currFast = currFast.next
        if ln % 2:
            mid = mid.next
        ln += 1

    pos = ln - n + 1
    halfCeil = -(-ln//2)
    if pos > halfCeil:
        return removeNth(head, mid, pos - halfCeil + 1, ln - halfCeil + 1)
    else:
        return removeNth(head, head, pos, ln)
