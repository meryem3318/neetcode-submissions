class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start_index: int, current_path: list[int], remaining: int):
            # Base Case 1: Target hit
            if remaining == 0:
                res.append(list(current_path))
                return
            
            # Base Case 2: Overshot target (prune branch)
            if remaining < 0:
                return

            for i in range(start_index, len(candidates)):
                # Choose
                current_path.append(candidates[i])
                
                # Explore (Pass 'i' instead of 'i + 1' to allow element reuse)
                backtrack(i, current_path, remaining - candidates[i])
                
                # Unchoose (Backtrack)
                current_path.pop()

        backtrack(0, [], target)
        return res