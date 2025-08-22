class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        x, y = 0, n
        while x < n:
            output.append(nums[x])
            output.append(nums[y])
            x += 1
            y += 1
        return output