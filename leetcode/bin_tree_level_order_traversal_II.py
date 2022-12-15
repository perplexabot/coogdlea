"""Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        from collections import defaultdict, deque

        d = defaultdict(list)

        def bfs(hd):
            Q = deque([(hd, 0)])
            while Q:
                curr, level = Q.popleft()
                d[level].append(curr.val)
                if curr.left:
                    Q.append((curr.left, level + 1))
                if curr.right:
                    Q.append((curr.right, level + 1))

        bfs(root)
        return [d[lvl] for lvl in reversed(range(len(d)))]


inps = [
    # ex0
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        [[3, 4, 4, 3], [2, 2], [1]],
    ),
    # ex1
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(7, None, None), None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        [[7], [3, 4, 4, 3], [2, 2], [1]],
    ),
    # ex2
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        [[4, 3, 4, 3], [2, 2], [1]],
    ),
    # ex3
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, TreeNode(3, None, None), None),
        ),
        [[3, 3], [2, 2], [1]],
    ),
    # ex4
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, TreeNode(4, None, None), None),
        ),
        [[3, 4], [2, 2], [1]],
    ),
    # ex5
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, None, TreeNode(3, None, None)),
        ),
        [[3, 3], [2, 2], [1]],
    ),
    # ex6
    (TreeNode(1, None, None), [[1]]),
    # ex7
    (None, []),
    # ex8
    (
        TreeNode(
            3,
            TreeNode(9, None, None),
            TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)),
        ),
        [[15, 7], [9, 20], [3]],
    ),
]

sol = Solution()
for ind, inp in enumerate(inps):
    print(f"Asserting example [{ind}]")
    assert inp[1] == sol.levelOrderBottom(inp[0])
