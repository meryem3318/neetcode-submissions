class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0  # 1. Return 0 (not True) so the +1 math works
            
            # 2. We must return the height so the parent call can receive it
            return 1 + max(height(root.right), height(root.left))
        
        if not root:
            return True
            
        # 3. Calculate heights of the root's children using your helper
        heightr = height(root.right)
        heightl = height(root.left)
        
        # Check if root is balanced AND recursively check if all subtrees are balanced too!
        return (abs(heightr - heightl) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)