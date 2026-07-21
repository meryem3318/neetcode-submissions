# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
# LCA is either the left node p itself in the case where its the LCA,
#for 2 given nodes, if they are siblings, then LCA is left it cant
#be parent because parent is bigger than left
# if for two nodes one is a child, if parent is on right side its itself
# if on right side, then LCA is parent of parent 
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
