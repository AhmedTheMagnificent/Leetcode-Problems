class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        if 0 in nums:
            if dic[0] > 1:
                return [0 for x in range(len(nums))]
            else:
                multiply = 1
                for i in nums:
                    if i == 0:
                        continue
                    else:
                        multiply *= i
                index = nums.index(0)
                output = [0 for x in nums]
                output[index] = multiply
                return output
        multiply = 1
        for i in nums:
            multiply *= i
        output = [multiply for i in nums]
        for i in range(len(nums)):
            output[i] = int(output[i]/nums[i])
        return output
            