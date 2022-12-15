"""Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True

        ls = []

        def bst_to_lst(rt):
            if rt.left:
                bst_to_lst(rt.left)
            ls.append(rt.val)
            if rt.right:
                bst_to_lst(rt.right)

        bst_to_lst(root)

        if len(ls) == 1:
            return True

        prev = ls[0]
        for i in range(1, len(ls)):
            if ls[i] <= prev:
                return False
            prev = ls[i]
        return True


ts = [
    (TreeNode(2, TreeNode(1), TreeNode(3)), True),
    (TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False),
    (TreeNode(3), True),
    (TreeNode(3, TreeNode(5)), False),
    (TreeNode(3, r=TreeNode(5)), True),
    (TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15)), True),
    (TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(11)), TreeNode(15)), False),
    (TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(5)), False),
    (TreeNode(10, TreeNode(5, TreeNode(5), TreeNode(7)), TreeNode(10)), False),
    (None, True),
    (TreeNode(1, TreeNode(1), None), False),
]

sol = Solution()
for ind, (rt, exp) in enumerate(ts):
    print(f"Doing t{ind} and asserting...")
    assert sol.isValidBST(rt) == exp
