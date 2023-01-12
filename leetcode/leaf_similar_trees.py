"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form
    a leaf value sequence.

For example, in the given tree above [not shown here], the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4],
            root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    Output: true

Example 2:
    Input: root1 = [1,2,3], root2 = [1,3,2]
    Output: false

Constraints:
    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].

A:
    if both empty -> return true
    if one empty -> return false
    assume values are ints (true according to constraint)

P:
    lvs1 = bfs(root1)
    lvs2 = bfs(root2)

    return lvs1 == lvs2
"""


def leafSimilar(root1, root2) -> bool:
    from collections import deque

    def get_lvs_dfs(root, lvs):
        if not root.left and not root.right:
            lvs.append(root.val)

        if root.left:
            get_lvs_dfs(root.left, lvs)
        if root.right:
            get_lvs_dfs(root.right, lvs)

    lvs1 = []
    get_lvs_dfs(root1, lvs1)
    lvs2 = []
    get_lvs_dfs(root2, lvs2)

    return lvs1 == lvs2
