from typing import List

class Solution:
    def count_less_equal(self, matrix: List[List[int]], target: int) -> int:
        """
        Count the number of elements less than or equal to the target in the matrix.
        """
        count = 0
        n = len(matrix)
        row, col = n - 1, 0  # Start from the bottom-left corner of the matrix
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                count += row + 1  # Add the entire column (from 0 to row)
                col += 1  # Move to the next column
            else:
                row -= 1  # Move to the previous row
        return count
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Find the kth smallest element in the matrix.
        """
        n = len(matrix)
        low = matrix[0][0]  # Minimum element in the matrix
        high = matrix[n - 1][n - 1]  # Maximum element in the matrix

        while low < high:
            mid = (low + high) // 2
            count = self.count_less_equal(matrix, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low