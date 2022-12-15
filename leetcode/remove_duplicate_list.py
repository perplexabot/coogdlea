"""Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x, nxt):
        self.val = x
        self.next = nxt


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def get_next_new(hd):
            v = hd.val
            curr = hd
            while curr and curr.val == v:
                curr = curr.next
            return curr

        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = get_next_new(curr.next)
            curr = curr.next
        return head


def print_list(hd):
    curr = hd
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print("\n")


sol = Solution()

inps = [
    ListNode(1, ListNode(1, ListNode(2, None))),
    ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None))))),
    ListNode(1, None),
    ListNode(1, ListNode(1, None)),
    ListNode(1, ListNode(1, ListNode(1, None))),
    ListNode(1, ListNode(2, ListNode(2, ListNode(3, None)))),
    ListNode(1, ListNode(1, ListNode(2, ListNode(2, None)))),
]

for i in inps:
    print("Doing list: ")
    print_list(i)
    ans = sol.deleteDuplicates(i)
    print(" ans: ")
    print_list(ans)
