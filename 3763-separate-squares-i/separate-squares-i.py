class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        eps = 1e-6
        y_min, y_max = 0, max([y + l for _, y, l in squares])
        
        while y_max - y_min > eps:
            mid = (y_min + y_max) / 2
            area_below = area_above = 0
            for x, y, l in squares:
                bottom = max(0, min(mid - y, l))
                top = max(0, l - bottom)
                area_below += bottom * l
                area_above += top * l
        
            if area_below < area_above:
                y_min = mid
            else:
                y_max = mid
        
        return mid
        