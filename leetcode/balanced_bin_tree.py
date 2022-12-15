"""Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def get_depth(nd, cnt):
            if not nd:
                return cnt
            cnt0 = get_depth(nd.left, cnt + 1)
            cnt1 = get_depth(nd.right, cnt + 1)
            return max(cnt0, cnt1)

        def isBalanced_helper(nd):
            if not nd:
                return True

            if abs(get_depth(nd.left, 0) - get_depth(nd.right, 0)) > 1:
                return False

            is_left_balanced = isBalanced_helper(nd.left)
            if not is_left_balanced:
                return False
            is_right_balanced = isBalanced_helper(nd.right)
            return is_right_balanced

        return isBalanced_helper(root)


inps = [
    (
        TreeNode(
            3,
            TreeNode(9, None, None),
            TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)),
        ),
        True,
    ),
    (
        TreeNode(
            1,
            TreeNode(
                2,
                TreeNode(3, TreeNode(4, None, None), TreeNode(4, None, None)),
                TreeNode(3, None, None),
            ),
            TreeNode(2, None, None),
        ),
        False,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(3, None, None)),
            TreeNode(2, None, TreeNode(3, None, None)),
        ),
        True,
    ),
    (TreeNode(1, None, None), True),
    (None, True),
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(7, None, None), None)),
            TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)),
        ),
        True,
    ),
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(7, None, None), None)),
            TreeNode(2, None, None),
        ),
        False,
    ),
]

sol = Solution()
for ind, inp in enumerate(inps):
    print(f"Asserting example[{ind}]..")
    assert sol.isBalanced(inp[0]) == inp[1]
