class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        map = {}
        lonelyNumbers = []
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        for num in nums:
            if map[num] == 1 and (num + 1) not in map and (num - 1) not in map:
                lonelyNumbers.append(num)
        return lonelyNumbers