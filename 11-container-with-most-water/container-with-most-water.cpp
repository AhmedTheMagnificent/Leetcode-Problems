class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxArea = 0;
        while(left < right){
            int area = (right - left) * min(height[left], height[right]);
            maxArea = max(area, maxArea);
            if(height[left] > height[right]) 
                right--;
            else   
                left++;
        }
        return maxArea;
    }
};