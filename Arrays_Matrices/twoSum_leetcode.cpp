// problem: https://leetcode.com/problems/two-sum
// TIME: O(n) - will only need to search at MAX all of the vector's elements to find the pair that sums up to target.
// SPACE: O(n) - utilized hashmap to store up to all the vector elements.
// - optimal solution, implemented in cpp.


#include <unordered_map>

class Solution {
public:
    
    // check if a key is in unordered_map
    bool checkKeyInUM(unordered_map<int,int>& um, int key){
        if(um.find(key) != um.end())
            return true; 
        return false;
    }
    
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numsIdx;
        
        for(int i=0; i< nums.size(); i++){
            int numToFind = target - nums[i];
            if(checkKeyInUM(numsIdx, numToFind) == true){
                return {i, numsIdx[numToFind]};
            }
            numsIdx[nums[i]] = i;
        }
        
        return {};
    }
};