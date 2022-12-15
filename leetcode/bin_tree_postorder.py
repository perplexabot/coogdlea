"""Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
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
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []

        def dfs(root):
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            pOrder.append(root.val)

        pOrder = []
        dfs(root)
        return pOrder


inps = [
    (TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None)), [3, 2, 1]),
    (TreeNode(3), [3]),
    (TreeNode(10, TreeNode(3), TreeNode(5)), [3, 5, 10]),
    (
        TreeNode(10, TreeNode(9, TreeNode(8, TreeNode(7, TreeNode(6), None), None), None), None),
        [6, 7, 8, 9, 10],
    ),
    (None, []),
]

sol = Solution()
for ind, (root, exp) in enumerate(inps):
    print(f"Doing test {ind} and asserting...")
    ans = sol.postorderTraversal(root)
    print(f" Got: ", ans)
    assert ans == exp
