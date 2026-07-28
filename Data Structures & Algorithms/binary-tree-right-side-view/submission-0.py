# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Handle the base case: an empty tree has an empty view.
        res = []
        if not root:
            return res
        
        # Standard BFS Queue setup: place the root node in the queue.
        # Queue will hold 'TreeNode' objects.
        q = deque([root])
        
        # Loop 1: While there are levels (nodes) to process.
        while q:
            # Step A: Measure how many nodes are in the *current* level.
            level_size = len(q)
            
            # Step B: Process exactly that many nodes (this row).
            # We use standard 0-indexing for 'i' (0 to level_size - 1).
            for i in range(level_size):
                # Pop the node from the LEFT side (First-In, First-Out).
                node = q.popleft()
                
                # Step C: The crucial identification step.
                # If 'i' is equal to the index of the last element,
                # then this node is the last node in the row.
                # We include it in our right-side view!
                if i == level_size - 1:
                    res.append(node.val)
                    
                # Step D: Always append children from LEFT to RIGHT.
                # This ensures the order remains correct for the *next* level.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return res
        