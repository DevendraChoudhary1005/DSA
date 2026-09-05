class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        top = 0
        bottom = rows-1

        while top <= bottom:
            middle = (top + bottom) // 2
            if target > matrix[middle][-1]:
                top = middle + 1
            elif target < matrix[middle][0]:
                bottom = middle - 1
            else:
                break

        if not top <= bottom:
            return False

        target_row = (top + bottom) // 2

        left = 0
        right = cols - 1

        while left <= right:
            middle = (left+right) // 2
            val = matrix[target_row][middle]
            if target == val:
                return True
            elif target > val:
                left = middle + 1
            elif target < val:
                right = middle - 1
            
        return False