class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low1, high1 = 0, len(matrix) - 1

        # Binary search over the rows to find the correct row
        while low1 <= high1:
            mid1 = (low1 + high1) // 2
            
            # Check if target can be in this row
            if matrix[mid1][-1] < target:
                low1 = mid1 + 1
            elif matrix[mid1][0] > target:
                high1 = mid1 - 1
            else:
                # Binary search in the row mid1
                low, high = 0, len(matrix[mid1]) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if matrix[mid1][mid] == target:
                        return True
                    elif matrix[mid1][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
                return False  # If the element is not found in the row
        return False  # If the row is not found
