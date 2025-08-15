class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if target < 0:
            return []
        output = []
        for i, num in enumerate(candidates):
            remainder = target - num
            for combination in self.combinationSum(candidates[i:], remainder):
                output.append([num] + combination)

        return output
