class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        values = set(nums)
        curr = {0}
        for _ in range(3):
            nxt = set()
            for x in curr:
                for v in values:
                    nxt.add(x ^ v)
                curr = nxt
        return len(curr)