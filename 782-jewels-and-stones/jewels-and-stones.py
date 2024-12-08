class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stoneMap = {}
        number = 0
        for stone in stones:
            if stone not in stoneMap:
                stoneMap[stone] = 1
            else:
                stoneMap[stone] += 1
        for jewel in jewels:
            if jewel in stoneMap:
                number += stoneMap[jewel]
        return number