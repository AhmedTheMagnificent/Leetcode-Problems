class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negativeNumbers = 0
        for i in grid:
            index = self.binarySearch(i)
            negativeNumbers += len(i) - index
        return negativeNumbers
    def binarySearch(self, arr):
        l, r = 0, len(arr) - 1
        while l <= r:
            middle = (l + r) // 2
            if arr[middle] < 0:
                r = middle - 1
            else:
                l = middle + 1
        return l
            