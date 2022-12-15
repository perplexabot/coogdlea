"""Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        from collections import deque

        def do_appends(nd, side, Q, lst):
            if getattr(nd, side):
                Q.append(getattr(nd, side))
                lst.append(getattr(nd, side).val)
            else:
                lst.append(None)

        def bfs(hd, reversed=False):
            vals = []
            if not hd:
                return vals
            Q = deque([hd])
            vals.append(hd.val)
            while Q:
                curr = Q.popleft()
                if reversed:
                    do_appends(curr, 'left', Q, vals)
                    do_appends(curr, 'right', Q, vals)
                else:
                    do_appends(curr, 'right', Q, vals)
                    do_appends(curr, 'left', Q, vals)
            return vals

        return bfs(root.left) == bfs(root.right, reversed=True)


sol = Solution()

inps = [
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        True,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(7, None, None), None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        False,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        False,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, TreeNode(3, None, None), None),
        ),
        True,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, TreeNode(4, None, None), None),
        ),
        False,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, None, TreeNode(3, None, None)),
        ),
        False,
    ),
    (TreeNode(1, None, None), True),
    (None, True),
]

for ind, (hd, expected) in enumerate(inps):
    ans = sol.isSymmetric(hd)
    print(f"Asserting test[{ind}]")
    assert ans == expected
print("ALL TEST CASES PASSED")
