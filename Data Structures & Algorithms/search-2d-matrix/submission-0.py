class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        # remember how to calculate column number
        n = len(matrix[0])
        low = 0
        high = m * n - 1

        # need to find a way to correspond number and matrix position

        while low <= high:
            mid = (low + high) // 2
            row = mid // n 
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            elif matrix[row][col] < target:
                low = mid + 1
        
        return False
        