"""Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth
of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 """
from random import randint

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def recurse_cre(s, e):
            if s < e:
                mid = s + ((e - s) // 2)
                nd = TreeNode(nums[mid])
                nd.left = recurse_cre(s, mid - 1)
                nd.right = recurse_cre(mid + 1, e)
                return nd
            elif e == s:
                return TreeNode(nums[s])
            else:
                return None

        return recurse_cre(0, len(nums) - 1)


def dfs_lst(hd, lst):
    if hd.left:
        dfs_lst(hd.left, lst)
    lst.append(hd.val)
    if hd.right:
        dfs_lst(hd.right, lst)


inps = [sorted([randint(-100, 100) for _ in range(randint(0, 5))]) for _ in range(10)]

sol = Solution()
for inp in inps:
    print(f"Converting {inp} to bst and asserting...")
    nd = sol.sortedArrayToBST(inp)
    vals = []
    if inp:
        dfs_lst(nd, vals)
    assert vals == inp
