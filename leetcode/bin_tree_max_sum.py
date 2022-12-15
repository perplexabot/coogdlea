"""Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3
Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7
Output: 42
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0

        ninf = float('-inf')
        m = [root.val]

        def maxPath(curr):
            if not curr.left and not curr.right:
                m[0] = max(m[0], curr.val)
                return curr.val
            leftPath = maxPath(curr.left) if curr.left else ninf
            rightPath = maxPath(curr.right) if curr.right else ninf
            maxSum = max(max(leftPath, rightPath) + curr.val, curr.val)
            m[0] = max(m[0], maxSum, leftPath + rightPath + curr.val)
            return maxSum

        maxPath(root)
        return m[0]


inps = [
    (TreeNode(1, TreeNode(2), TreeNode(3)), 6),
    (TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 42),
    (None, 0),
    (TreeNode(100), 100),
    (TreeNode(-50, TreeNode(50), TreeNode(50)), 50),
    (TreeNode(50, TreeNode(-50), TreeNode(-20)), 50),
    (TreeNode(50, TreeNode(50), TreeNode(50)), 150),
    (TreeNode(50, TreeNode(50), None), 100),
    (TreeNode(50, None, TreeNode(50)), 100),
    (TreeNode(-10, TreeNode(20), TreeNode(50)), 60),
    (TreeNode(-1, TreeNode(5, TreeNode(4, None, TreeNode(2, TreeNode(-4), None)), None), None), 11),
    (
        TreeNode(
            -1,
            TreeNode(8, None, TreeNode(-9)),
            TreeNode(
                2, TreeNode(0, TreeNode(-3, None, TreeNode(-9, None, TreeNode(2))), None), None
            ),
        ),
        9,
    ),
]

sol = Solution()
for ind, (hd, exp) in enumerate(inps):
    print(f"Finding maxpathsum for input[{ind}] and asserting...")
    ans = sol.maxPathSum(hd)
    print(f" Got: ", ans)
    assert ans == exp
