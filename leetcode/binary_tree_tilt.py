"""
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values
and all right subtree node values. If a node does not have a left child, then the sum of the left
subtree node values is treated as 0. The rule is similar if the node does not have a right child.

Example 1:
    Input: root = [1,2,3]
    Output: 1
    Explanation:
    Tilt of node 2 : |0-0| = 0 (no children)
    Tilt of node 3 : |0-0| = 0 (no children)
    Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just
        right child, so sum is 3)
    Sum of every tilt : 0 + 0 + 1 = 1

Example 2:
    Input: root = [4,2,9,3,5,null,7]
    Output: 15
    Explanation:
    Tilt of node 3 : |0-0| = 0 (no children)
    Tilt of node 5 : |0-0| = 0 (no children)
    Tilt of node 7 : |0-0| = 0 (no children)
    Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just
        right child, so sum is 5)
    Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child,
        so sum is 7)
    Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which
        sums to 10; right subtree values are 9 and 7, which sums to 16)
    Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15

Example 3:
    Input: root = [21,7,14,1,1,2,2,3,3]
    Output: 9

Constraints:
    The number of nodes in the tree is in the range [0, 10**4].
    -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

A:
    tree with only root ->  return 0
    tree with root and left child -> tilt of left-child = 0, tilt of root = left-child.value return sum

D:
    if not root.left and not root.right:
        return 0

    save = dict()
    def tree_sum(node, sum):
        if node in save:
            return save[node]

        q = [node]
        sum = 0
        while q:
            curr = q.pop()
            sum += curr.val
            if curr.left:
                q.push(curr.left)
            if curr.right:
                q.push(curr.left)
        save[node] = sum
        return sum

    tilts = []
    def allTilts(node):
        q = [node]
        while q:
            curr = q.popleft()
            if not node.left and not node.right:
                tilts.append(0)
            if not node.left:
                tilts.append(abs(0 - treesum(node.right)))
            if not node.right:
                tilts.append(abs(treesum(node.left) - 0))
            tilts.append(abs(tree_sum(node.left) - tree_sum(node.right)))
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0

        def tree_sum(node):
            total = 0
            q = deque([node])
            while q:
                curr = q.popleft()
                total += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            return total

        def all_tilts(node):
            q = deque([node])
            tilts = []
            while q:
                curr = q.popleft()
                if not curr.left and not curr.right:
                    tilts.append(0)
                elif not curr.left and curr.right:
                    tilts.append(abs(0 - tree_sum(curr.right)))
                    q.append(curr.right)
                elif not curr.right and curr.left:
                    tilts.append(abs(tree_sum(curr.left) - 0))
                    q.append(curr.left)
                else:
                    tilts.append(abs(tree_sum(curr.left) - tree_sum(curr.right)))
                    q.append(curr.left)
                    q.append(curr.right)
            return tilts

        return sum(all_tilts(root))


cases = [
    (TreeNode(1, TreeNode(2), TreeNode(3)), 1),
    (TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7))), 15),
]

sol = Solution()
for index, (root, exp) in enumerate(cases):
    assert (got := sol.findTilt(root)) == exp, f"Failed case {index} - expecting {exp}, got {got}."
