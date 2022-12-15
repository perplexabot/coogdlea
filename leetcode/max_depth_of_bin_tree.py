"""Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down
to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def maxDepth_helper(hd, cnt):
            if not hd:
                return cnt

            cnt += 1
            cnt0 = maxDepth_helper(hd.left, cnt) if hd.left else cnt
            cnt1 = maxDepth_helper(hd.right, cnt) if hd.right else cnt
            return max(cnt0, cnt1)

        return maxDepth_helper(root, 0)


inps = [
    # 0
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        3,
    ),
    # 1
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(7, None, None), None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        4,
    ),
    # 2
    (
        TreeNode(
            3,
            TreeNode(9, None, None),
            TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)),
        ),
        3,
    ),
    # 3
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, None, None), None), None), None),
            None,
        ),
        5,
    ),
    # 4
    (TreeNode(1, None, None), 1),
    # 5
    (TreeNode(0, TreeNode(1, None, None), TreeNode(2, None, None)), 2),
    # 6
    (None, 0),
]

sol = Solution()
for ind, inp in enumerate(inps):
    print(f"Asserting example[{ind}], expecting ({inp[1]})")
    assert sol.maxDepth(inp[0]) == inp[1]
