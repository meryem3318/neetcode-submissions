class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Look at every single row (using len(matrix) ensures we don't skip the last row)
        for m in range(len(matrix)):
            
            # 2. Check if the target falls within this row's boundaries
            if matrix[m][0] <= target <= matrix[m][-1]:
                
                # 3. If it does, check if the target exists on this "floor"
                if target in matrix[m]:
                    return True
                
                return False
                
        return False