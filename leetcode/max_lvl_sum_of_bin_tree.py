"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2,
and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
    Input: root = [1,7,0,7,-8,null,null]
    Output: 2
    Explanation:
    Level 1 sum = 1.
    Level 2 sum = 7 + 0 = 7.
    Level 3 sum = 7 + -8 = -1.
    So we return the level with the maximum sum which is level 2.

Example 2:
    Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
    Output: 2

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -105 <= Node.val <= 105

URL: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
START: 23:33

ADAPOCT

    A
        null root: 0
        no children: 1

    D
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import deque, defaultdict

        cnts = defaultdict(int)
        Q = deque([(root, 1)])
        while Q:
            curr, lvl = Q.popleft()
            cnts[lvl] += curr.val

            if curr.left:
                Q.append((curr.left, lvl + 1))
            if curr.right:
                Q.append((curr.right, lvl + 1))

        max_l = 1
        for l in cnts:
            if cnts[l] > cnts[max_l]:
                max_l = l
        return max_l


inps = [
    (TreeNode(), 1),
    (
        TreeNode(
            1,
            TreeNode(7, TreeNode(7, None, None), TreeNode(-8, None, None)),
            TreeNode(0, None, None),
        ),
        2,
    ),
]

sol = Solution()

test = 0
for root, exp in inps:
    assert (ans := sol.maxLevelSum(root)) == exp, f"failed test-{test}: got {ans} expecting {exp}"
    test += 1
