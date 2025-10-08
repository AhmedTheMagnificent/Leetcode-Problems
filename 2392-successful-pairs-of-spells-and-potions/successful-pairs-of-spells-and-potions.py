class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        output = []
        for spell in spells:
            l, r = 0, len(potions) - 1
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] * spell >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            output.append(n - l)
        return output