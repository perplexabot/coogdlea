"""Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque

        if not root:
            return 0

        def bfs(hd):
            Q = deque([(hd, 1)])
            while Q:
                curr, lvl = Q.popleft()
                if not curr.left and not curr.right:
                    return lvl

                if curr.left:
                    Q.append((curr.left, lvl + 1))

                if curr.right:
                    Q.append((curr.right, lvl + 1))

        return bfs(root)


inps = [
    (
        TreeNode(
            3,
            TreeNode(9, None, None),
            TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)),
        ),
        2,
    ),
    (TreeNode(3, TreeNode(9, None, None), None), 2),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, None, None), None), None), None), 4),
    (None, 0),
    (TreeNode(1, None, None), 1),
]

sol = Solution()
for ind, inp in enumerate(inps):
    print(f'Finding min depth for example[{ind}] and asserting...')
    print(f' answer found to be {sol.minDepth(inp[0])}')
    assert inp[1] == sol.minDepth(inp[0])
