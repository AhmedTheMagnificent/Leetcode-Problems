class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lis = sorted([str(i) for i in range(1, n+1)])
        return [int(i) for i in lis]
        