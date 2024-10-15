class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> positive;
        vector<int> negative;
        for(int num : nums){
            if(num > 0){
                positive.push_back(num);
            }
            else{
                negative.push_back(num);
            }
        }
        for(int i = 0, p = 0, n = 0; i < nums.size(); i+=2){
            nums[i] = positive[p++];
            nums[i+1] = negative[n++];
        }
        return nums;
    }
};