class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, current_max: int) -> int:
            if not node:
                return 0
            
            good_count = 0
            if node.val >= current_max:
                good_count = 1
            
            new_path_max = max(current_max, node.val)
            
            left_results = dfs(node.left, new_path_max)
            right_results = dfs(node.right, new_path_max)
            
            return good_count + left_results + right_results

        return dfs(root, root.val)