class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonal = -float('inf')
        maxArea = -float('inf')
        for l, w in dimensions:
            diagonal = l ** 2 + w ** 2
            area = l * w
            if diagonal > maxDiagonal or (diagonal == maxDiagonal and area > maxArea):
                maxDiagonal = diagonal
                maxArea = area
        return maxArea