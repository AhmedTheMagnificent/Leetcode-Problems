class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            rows = []
            for j in range(i+1):
                if j == 0 or j == i:
                    rows.append(1)
                else:
                    rows.append(result[i-1][j-1] + result[i-1][j])
            result.append(rows)
        return result
        