# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. Base cases for scanning
        if not subRoot: 
            return True  # An empty tree is always a subtree of anything
        if not root: 
            return False # We ran out of main tree, so we didn't find the subtree

        # 2. Check if the current node matches subRoot
        if self.isSameTree(root, subRoot):
            return True

        # 3. If it didn't match, search down the left and right children recursively!
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Helper function: Checks if two trees are completely identical in structure and values
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are empty, they are the same
        if not p and not q:
            return True
        # If only one is empty, or their values don't match, they aren't the same
        if not p or not q or p.val != q.val:
            return False
            
        # Recurse down both left and right sides to check the rest of the tree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)