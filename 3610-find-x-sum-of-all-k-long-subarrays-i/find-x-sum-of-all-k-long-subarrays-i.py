class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        output = []
        for i in range(len(nums) - k + 1):
            d = Counter(nums[i:i+k])
            sorte = sorted(d.items(), key=lambda pair: (-pair[1], -pair[0]))
            val = sum(k * v for k, v in sorte[:x])
            output.append(val)
        return output