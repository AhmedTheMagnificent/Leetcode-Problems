class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        output = {}

        for r in range(rows):
            for c in range(cols):
                dist = abs(rCenter - r) + abs(cCenter - c)
                if dist not in output:
                    output[dist] = []
                output[dist].append([r, c])

        result = []
        for key in sorted(output.keys()):
            result.extend(output[key])

        
        return result