class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        minDistance = float('inf')
        
        if abs(x - z) < minDistance:
            person = 1
            minDistance = abs(x - z)
        if abs(y - z) < minDistance:
            person = 2
        if abs(x - z) == abs(y - z):
            person = 0
        return person 