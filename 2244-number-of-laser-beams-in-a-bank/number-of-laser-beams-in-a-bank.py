class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        prev = 0
        for row in bank:
            curr = row.count("1")
            if curr == 0:
                continue
            count += prev * curr
            prev = curr
        return count