class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        maxProduct = float('-inf')
        
        currProd_Left_to_Right = 1

        for i in range(0,n):
            currProd_Left_to_Right*=nums[i]

            maxProduct = max(maxProduct, currProd_Left_to_Right)
            
            if currProd_Left_to_Right == 0:
                currProd_Left_to_Right = 1

        currProd_Right_to_Left = 1

        for i in range(n-1,-1,-1):
            currProd_Right_to_Left*=nums[i]
            
            maxProduct = max(maxProduct, currProd_Right_to_Left)
            
            if currProd_Right_to_Left == 0:
                currProd_Right_to_Left = 1
            

    
        return maxProduct