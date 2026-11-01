class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       unordered_map<int,int> prev_map;
       for (int i = 0; i< nums.size(); i++){
        int diff = target - nums[i];
        if (prev_map.contains(diff)){
            return {prev_map[diff],i};
        }
        prev_map[nums[i]] = i ;
       } 
       return {};
    }
};
