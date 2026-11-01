class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       int num_size = nums.size();
       unordered_map<int,int> prev_map;
       for (int i = 0; i< num_size; i++){
        int diff = target - nums[i];
        if (prev_map.find(diff) != prev_map.end()){
            return {prev_map[diff],i};
        }
        prev_map.insert({nums[i],i});
       } 
       return {};
    }
};
