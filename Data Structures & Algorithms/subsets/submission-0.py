class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start_index: int, current_path: list[int]):
            res.append(list(current_path))

            for i in range(start_index, len(nums)):
                current_path.append(nums[i])

                backtrack(i+1, current_path)

                current_path.pop()

        backtrack(0, [])
        return res
sol = Solution()
print(sol.subsets([1, 2, 3]))

        