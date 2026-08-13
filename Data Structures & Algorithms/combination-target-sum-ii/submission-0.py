class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            value_to_skip = candidates[i]
            while i < len(candidates) and candidates[i] == value_to_skip:
                i += 1
            dfs(i, cur, total)
        dfs(0, [], 0)
        return res
            
            
        