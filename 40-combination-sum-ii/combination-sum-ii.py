class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if target == 0:
            return [[]]
        if target < 0:
            return []
        
        output = []
        for i, num in enumerate(candidates):
            if i > 0 and num == candidates[i - 1]:
                continue
            remainder = target - num
            for combination in self.combinationSum2(candidates[i + 1:], remainder):
                output.append([num] + combination)
        return output
        