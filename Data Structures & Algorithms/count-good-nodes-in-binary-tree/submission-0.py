# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # This function handles standard tree traversal (DFS, specifically Preorder),
        # but it MUST carry one vital extra state: 'current_max'.
        # This represents the largest value seen on THIS specific path.
        def dfs(node: TreeNode, current_max: int) -> int:
            # Base Case: We have recursed past a leaf onto an empty child.
            # Empty nodes can't be good. Return 0 to our parent.
            if not node:
                return 0
            
            # Identify if the *current node* itself is good.
            # Initialized to 0. It is a "good node" if its value is equal to
            # or greater than the highest value seen *above* it on this path.
            good_count = 0
            if node.val >= current_max:
                good_count = 1  # We found a good node! Mark it.
            
            # Step B: Determine the maximum value for the subsequent path (our children).
            # We include the current node in the assessment of the new path max.
            # (e.g., Path (3)->(1): max is 3. Path (3)->(4): max is 4.)
            new_path_max = max(current_max, node.val)
            
            # Step C: Recurse Both Sides.
            # CRUCIAL: Pass the updated 'new_path_max' down. This preserves the 
            # independent path state required for the calculation.
            left_side_results = dfs(node.left, new_path_max)
            right_side_results = dfs(node.right, new_path_max)
            
            # Step D: Collate the results.
            # Return our node's goodness state + the good count from left sub-trees
            # + the good count from right sub-trees.
            return good_count + left_side_results + right_side_results

        # Step 1: Initial Call: Start at the root.
        # The 'current_max' on the path starting at the root is root.val itself.
        return dfs(root, root.val)