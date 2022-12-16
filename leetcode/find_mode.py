"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the
    most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's
    key. Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [1,null,2,2]
    Output: [2]

Example 2:
    Input: root = [0]
    Output: [0]

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -105 <= Node.val <= 105

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space
    incurred due to recursion does not count).

A:
    root is none -> return []

D:
    [1,null,2,2]
    bfs:
        1, cnt = {1:1}
        2, cnt = {1:1, 2:1}
        2, cnt = {1:1, 2:2}
    return 2

P:
    cnts = Counter()
    bfs(root, cnts)
    return all maxes of cnts
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root) -> list[int]:
    from collections import Counter, deque

    cnts = Counter()
    Q = deque([root])
    while Q:
        curr = Q.popleft()
        cnts.update([curr.val])

        if curr.left:
            Q.append(curr.left)
        if curr.right:
            Q.append(curr.right)

    mode = cnts[max(cnts, key=lambda x: cnts[x])]
    return [k for k in cnts if cnts[k] == mode]


T0 = TreeNode(1, None, TreeNode(2, TreeNode(2), None))
T1 = TreeNode(1, None, None)
T2 = TreeNode(1, TreeNode(1), TreeNode(1))
T4 = TreeNode(1, TreeNode(2), TreeNode(3))
T5 = TreeNode(0, None, TreeNode(0))

T6left = TreeNode(0, TreeNode(0, TreeNode(), None), TreeNode(0))
T6right = TreeNode(1, TreeNode(1), TreeNode(1))
T6 = TreeNode(1, T6left, T6right)

T7left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(2), TreeNode(6)))
T7right = TreeNode(8, TreeNode(7), TreeNode(9))
T7 = TreeNode(6, T7left, T7right)

cases = [
    (T0, [2]),
    (T1, [1]),
    (T2, [1]),
    (T4, [1, 2, 3]),
    (None, []),
    (T5, [0]),
    (T6, [0, 1]),
    (T7, [2, 6]),
]

for (root, exp) in cases:
    assert sorted(got := findMode(root)) == sorted(
        exp
    ), f"Failed with {root} - got {got}, expecting {exp}"
