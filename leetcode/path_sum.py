"""Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding
up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        def dfs(hd, curr_sum):

            if not hd.left and not hd.right:
                if curr_sum == sum:
                    return True
                else:
                    return False
            else:
                right_bool, left_bool = False, False
                if hd.right:
                    right_bool = dfs(hd.right, curr_sum + hd.right.val)
                if hd.left:
                    left_bool = dfs(hd.left, curr_sum + hd.left.val)
                return right_bool or left_bool

        return dfs(root, root.val)


inps = [
    (TreeNode(5, None, None), 5, True),
    (
        TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7, None, None), TreeNode(2, None, None)), None),
            TreeNode(8, TreeNode(13, None, None), TreeNode(4, None, TreeNode(18, None, None))),
        ),
        22,
        True,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        6,
        True,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(7, None, None), None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        14,
        True,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        9,
        False,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, TreeNode(3, None, None), None),
        ),
        1,
        False,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, TreeNode(4, None, None), None),
        ),
        7,
        True,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, None, TreeNode(3, None, None)),
        ),
        66,
        False,
    ),
    (TreeNode(1, None, None), 0, False),
    (TreeNode(1, None, None), 1, True),
    (None, 33, False),
]

sol = Solution()

for ind, (hd, sm, expected) in enumerate(inps):
    print(f'Checking if {sm} exists as a path in example[{ind}] and asserting...')
    assert expected == sol.hasPathSum(hd, sm)
