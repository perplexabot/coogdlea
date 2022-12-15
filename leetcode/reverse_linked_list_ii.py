"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]

Example 2:
    Input: head = [5], left = 1, right = 1
    Output: [5]

Constraints:
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n


Follow up: Could you do it in one pass?

URL: https://leetcode.com/problems/reverse-linked-list-ii/

START: 6:00

A
    if left == right: do nothing
    if head is null: return head
    if head is single: return head

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right or not head:
            return head

        lefti = left - 1
        righti = right - 1
        curr = head
        prev = None
        cnt = 0

        while curr:
            if cnt == lefti:
                before_left = prev
                left_node = curr

            if cnt == righti:
                after_right = curr.next if curr.next else None
                right_node = curr

            n = curr.next
            if cnt >= lefti and cnt <= righti:
                curr.next = prev if prev else None
            prev = curr
            curr = n
            cnt += 1

        if before_left:
            before_left.next = right_node
        left_node.next = after_right

        return head if lefti != 0 else right_node


def print_list(h):
    curr = h
    stop = 10
    cnt = 0
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
        if cnt == stop:
            break
        cnt += 1
    print()


ex1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
ex2 = ListNode(5, None)
ex3 = ListNode(3, ListNode(5, None))

inps = [(None, 1, 4), (ex1, 2, 4), (ex2, 1, 1), (ex3, 1, 2)]
sol = Solution()

for head, left, right in inps:
    print('-----------------------------')
    print_list(head)
    ans = sol.reverseBetween(head, left, right)
    print_list(ans)
