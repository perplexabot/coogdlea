class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def addLinkedLists(l0, l1):
    currl0 = l0
    currl1 = l1
    carry = 0
    dig0 = 0
    dig1 = 0
    ans = None

    while currl0 or currl1:
        if not currl0:
            dig0 = 0
        else:
            print '\nsetting d0 to: ', currl0.val
            dig0 = currl0.val

        if not currl1:
            dig1 = 0
        else:
            print 'setting d1 to: ', currl1.val
            dig1 = currl1.val


        num = dig0 + dig1 + carry
        carry = num // 10
        numOnes = num % 10
        print '\nd0: ', dig0
        print 'd1: ', dig1
        print 'num: ', num
        print 'car: ', carry
        print 'one: ', numOnes
        if currl0:
            currl0 = currl0.next
        if currl1:
            currl1 = currl1.next

        if ans is None:
            ans = ListNode(numOnes)
        else:
            tmp = ListNode(numOnes)
            tmp.next = ans
            ans = tmp

        return ans

def printList(n):
    while n:
        print n.val, 
        n = n.next
temp = ListNode(3)
curr = ListNode(4)
curr.next = temp
temp = ListNode(2) 
temp.next = curr
l0 = temp


temp = ListNode(4)
curr = ListNode(6)
curr.next = temp
temp = ListNode(5) 
temp.next = curr
l1 = temp

print 'l0: ', 
printList(l0)
print '\nl1: ', 
printList(l1)

a = addLinkedLists(l0,l1)
print '\nAns: ',
printList(a)
