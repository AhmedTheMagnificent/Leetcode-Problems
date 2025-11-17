class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = k  # pretend we've already seen enough zeros before first 1
        
        for num in nums:
            if num == 1:
                if dist < k:
                    return False
                dist = 0
            else:
                dist += 1
                
        return True
            