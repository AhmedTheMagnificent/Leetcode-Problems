class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector <int> result(nums.size(), 0);
        int left = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] < pivot){
                result[left] = nums[i];
                left++;
            }
        }
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == pivot){
                result[left] = nums[i];
                left++;
            }
        }
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > pivot){
                result[left] = nums[i];
                left++;
            }
        }
        return result;
    }
};