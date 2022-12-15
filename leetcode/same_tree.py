"""Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes
have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p and not q) or (q and not p):
            return False

        from collections import deque

        def do_appends(Q, curr):
            appends = 0
            if curr.left:
                appends += 1
                Q.append(curr.left)
            if curr.right:
                appends += 2
                Q.append(curr.right)
            return appends

        def bfs_cmp(hd0, hd1):
            Q0 = deque([hd0]) if hd0 else deque([])
            Q1 = deque([hd1]) if hd1 else deque([])
            while Q0 and Q1:
                curr0 = Q0.popleft()
                curr1 = Q1.popleft()
                if curr0.val != curr1.val:
                    return False
                if do_appends(Q0, curr0) != do_appends(Q1, curr1):
                    return False
            return True

        return bfs_cmp(p, q)


sol = Solution()

inps = [
    (None, None, True),
    (
        TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None)),
        TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None)),
        True,
    ),
    (
        TreeNode(1, TreeNode(2, None, None), TreeNode(1, None, None)),
        TreeNode(1, TreeNode(1, None, None), TreeNode(2, None, None)),
        False,
    ),
    (TreeNode(1, None, None), TreeNode(2, None, None), False),
    (TreeNode(1, None, None), TreeNode(1, None, None), True),
    (TreeNode(1, None, None), None, False),
    (TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None)), None, False),
    (TreeNode(1, TreeNode(2, None, None), None), TreeNode(1, None, TreeNode(2, None, None)), False),
]
for ind, inp in enumerate(inps):
    ans = sol.isSameTree(inp[0], inp[1])
    print(f"Doing example {ind}: {ans}")
    assert inp[2] == ans
