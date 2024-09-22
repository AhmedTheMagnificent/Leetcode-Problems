class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> indices;
        for(int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if(indices.find(complement) == indices.end()){
                indices[nums[i]] = i; 
            }
            else{
                return {indices[complement], i};
            }
        }
        return {};
    }
};